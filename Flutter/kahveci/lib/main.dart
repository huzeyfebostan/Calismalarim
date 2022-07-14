import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

void main() {
  runApp(
    MyWid(),
  );
}

class MyWid extends StatelessWidget {
  const MyWid({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.brown[300],
        body: SafeArea(
          child: Center(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: <Widget>[
                CircleAvatar(
                  radius: 70.0,
                  backgroundColor: Colors.lime,
                  backgroundImage: AssetImage('assets/images/kahve.jpeg'),
                ),
                Text(
                  'Flutter Kahvecisi',
                  style: TextStyle(
                      fontFamily: 'Satisfy',
                      fontSize: 45,
                      color: Colors.brown[900]),
                ),
                Text(
                  'BİR FİNCAN UZAĞINIZDA',
                  style: GoogleFonts.dancingScript(
                      fontSize: 26, color: Colors.white),
                ),
                Container(
                  margin: const EdgeInsets.symmetric(
                    horizontal: 45.0,
                  ),
                  padding: const EdgeInsets.all(10.0),
                  color: Colors.brown[900],
                  child: Row(
                    children: const <Widget>[
                      Icon(
                        Icons.email,
                        color: Colors.white,
                      ),
                      SizedBox(
                        width: 10.0,
                      ),
                      Text(
                        'siparis@fkahvecisi.com',
                        style: TextStyle(
                          color: Colors.white,
                          fontSize: 20,
                        ),
                      ),
                    ],
                  ),
                ),
                const SizedBox(
                  height: 10,
                ),
                Container(
                  margin: const EdgeInsets.symmetric(
                    horizontal: 45.0,
                  ),
                  padding: const EdgeInsets.all(10.0),
                  color: Colors.brown[900],
                  child: Row(
                    children: const <Widget>[
                      Icon(
                        Icons.phone,
                        color: Colors.white,
                      ),
                      SizedBox(
                        width: 10.0,
                      ),
                      Text(
                        '+90 555 555 55 55',
                        style: TextStyle(
                          color: Colors.white,
                          fontSize: 20,
                        ),
                      )
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
