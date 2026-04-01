import 'package:flutter/material.dart';

class PredictionScreen extends StatefulWidget {
  const PredictionScreen({super.key});

  @override
  State<PredictionScreen> createState() => _PredictionScreenState();
}

class _PredictionScreenState extends State<PredictionScreen> {
  final _formKey = GlobalKey<FormState>();
  double _rainfall = 0.0;
  double _humidity = 0.0;
  double _temp = 0.0;

  String? _riskResult;
  double? _scoreResult;

  void _submitForm() {
    if (_formKey.currentState!.validate()) {
      _formKey.currentState!.save();
      // Placeholder: In a real app we perform an HTTP POST request to /predict
      // Mock result:
      setState(() {
         double mockScore = (_rainfall * 0.5 + _humidity * 0.3 + (40 - _temp).clamp(0, 40) * 0.2) / 100.0;
         _scoreResult = mockScore.clamp(0.0, 1.0);
         _riskResult = _scoreResult! > 0.7 ? "High" : (_scoreResult! > 0.4 ? "Medium" : "Low");
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Flood Prediction')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Form(
              key: _formKey,
              child: Column(
                children: [
                  TextFormField(
                    decoration: const InputDecoration(labelText: 'Rainfall (mm)'),
                    keyboardType: TextInputType.number,
                    onSaved: (val) => _rainfall = double.parse(val ?? '0'),
                  ),
                  TextFormField(
                    decoration: const InputDecoration(labelText: 'Humidity (%)'),
                    keyboardType: TextInputType.number,
                    onSaved: (val) => _humidity = double.parse(val ?? '0'),
                  ),
                  TextFormField(
                    decoration: const InputDecoration(labelText: 'Temperature (°C)'),
                    keyboardType: TextInputType.number,
                    onSaved: (val) => _temp = double.parse(val ?? '0'),
                  ),
                  const SizedBox(height: 20),
                  ElevatedButton(
                    onPressed: _submitForm,
                    child: const Text('Predict Risk'),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 40),
            if (_riskResult != null)
              Card(
                color: _riskResult == 'High' ? Colors.red.shade100 : Colors.green.shade100,
                child: Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: Column(
                    children: [
                      Text("Risk Level: $_riskResult", style: const TextStyle(fontSize: 24, fontWeight: FontWeight.bold)),
                      Text("Probability: ${(_scoreResult! * 100).toStringAsFixed(1)}%"),
                    ],
                  ),
                ),
              )
          ],
        ),
      ),
    );
  }
}
