import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:provider/provider.dart';

import 'screens/home_screen.dart';
import 'screens/prediction_screen.dart';
import 'screens/chatbot_screen.dart';
import 'screens/map_screen.dart';

void main() {
  runApp(const AquaShieldApp());
}

class LanguageProvider extends ChangeNotifier {
  Locale _currentLocale = const Locale('en');

  Locale get currentLocale => _currentLocale;

  void toggleLanguage() {
    _currentLocale = _currentLocale.languageCode == 'en' 
        ? const Locale('ta') 
        : const Locale('en');
    notifyListeners();
  }
}

class AquaShieldApp extends StatelessWidget {
  const AquaShieldApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (_) => LanguageProvider(),
      child: Consumer<LanguageProvider>(
        builder: (context, langProvider, child) {
          return MaterialApp(
            title: 'AquaShield AI',
            debugShowCheckedModeBanner: false,
            locale: langProvider.currentLocale,
            supportedLocales: const [
              Locale('en', ''), // English
              Locale('ta', ''), // Tamil
            ],
            localizationsDelegates: const [
              GlobalMaterialLocalizations.delegate,
              GlobalWidgetsLocalizations.delegate,
              GlobalCupertinoLocalizations.delegate,
            ],
            theme: ThemeData(
              brightness: Brightness.light,
              primarySwatch: Colors.blue,
              useMaterial3: true,
            ),
            darkTheme: ThemeData(
              brightness: Brightness.dark,
              primarySwatch: Colors.blue,
              useMaterial3: true,
            ),
            themeMode: ThemeMode.system,
            initialRoute: '/',
            routes: {
              '/': (context) => const HomeScreen(),
              '/predict': (context) => const PredictionScreen(),
              '/chat': (context) => const ChatbotScreen(),
              '/map': (context) => const MapScreen(),
            },
          );
        },
      ),
    );
  }
}
