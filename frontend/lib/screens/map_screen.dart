import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';

class MapScreen extends StatefulWidget {
  const MapScreen({super.key});

  @override
  State<MapScreen> createState() => _MapScreenState();
}

class _MapScreenState extends State<MapScreen> {
  // Center of Chennai arbitrarily chosen for simulation testing
  static const LatLng _center = LatLng(13.0827, 80.2707);

  final Set<Marker> _markers = {};
  final Set<Circle> _circles = {};

  @override
  void initState() {
    super.initState();
    // Setup Mock Heatmap circles
    _circles.add(
      Circle(
        circleId: const CircleId('risk_zone_1'),
        center: const LatLng(13.0827, 80.2707),
        radius: 2000, // 2km radius
        fillColor: Colors.red.withAlpha(100),
        strokeColor: Colors.red,
        strokeWidth: 1,
      )
    );
     _circles.add(
      Circle(
        circleId: const CircleId('risk_zone_2'),
        center: const LatLng(13.0900, 80.2500),
        radius: 1000, 
        fillColor: Colors.yellow.withAlpha(100),
        strokeColor: Colors.yellow,
        strokeWidth: 1,
      )
    );
  }

  void _onMapCreated(GoogleMapController controller) {
    // We would fetch real data from /simulate here
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Flood Risk Map')),
      body: GoogleMap(
        onMapCreated: _onMapCreated,
        initialCameraPosition: const CameraPosition(
          target: _center,
          zoom: 12.0,
        ),
        markers: _markers,
        circles: _circles,
        myLocationEnabled: true,
      ),
    );
  }
}
