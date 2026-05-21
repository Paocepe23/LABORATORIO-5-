void setup() {
  Serial.begin(115200);
  pinMode(10, INPUT); // LO+
  pinMode(11, INPUT); // LO-
}

void loop() {
  if (digitalRead(10) == 1 || digitalRead(11) == 1) {
    Serial.println("!");  // electrodo despegado
  } else {
    Serial.println(analogRead(A0));  // enviar valor ECG
  }
  delay(10);  // 100 Hz
}