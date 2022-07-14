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
                const CircleAvatar(
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
                      fontSize: 20, color: Colors.white),
                ),
                Container(
                  width: 230,
                  child: Divider(
                    height: 10,
                    color: Colors.brown[900],
                  ),
                ),
                Card(
                    margin: const EdgeInsets.symmetric(
                      horizontal: 45.0,
                    ),
                    color: Colors.brown[900],
                    child: const ListTile(
                      leading: Icon(
                        Icons.email,
                        color: Colors.white,
                      ),
                      title: Text(
                        'siparis@fkahvecisi.com',
                        style: TextStyle(
                          color: Colors.white,
                          fontSize: 17.0,
                        ),
                      ),
                    )),
                const SizedBox(
                  height: 10,
                ),
                Card(
                  margin: const EdgeInsets.symmetric(
                    horizontal: 45.0,
                  ),
                  color: Colors.brown[900],
                  child: const ListTile(
                    leading: Icon(
                      Icons.phone,
                      color: Colors.white,
                    ),
                    title: Text(
                      '+90 555 555 55 55',
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 17.0,
                      ),
                    ),
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
