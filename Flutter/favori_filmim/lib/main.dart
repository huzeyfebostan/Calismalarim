import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    home: Scaffold(
      backgroundColor: Color(0xFFBDBDBD),
      appBar: AppBar(
        centerTitle: true,
        backgroundColor: Colors.cyanAccent[900],
        title: Text('Favori Filmim'),
      ),
      body: Center(child: Image.asset('images/inception.jpg')),
    ),
  ));
}
