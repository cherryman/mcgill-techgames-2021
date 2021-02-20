import { StatusBar } from "expo-status-bar";
import React, { useState, useCallback, useRef, useEffect } from "react";
import {
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
  Button,
  Alert,
} from "react-native";

export default function App() {
  const [running, setRunning] = useState<boolean>(false);
  const [elapsed, setElapsed] = useState<number>(0);
  const timeOrigin = useRef<number>(Date.now());
  const intervalId = useRef<any>();

  const onPress = () => {
    if (!running) {
      // running
      setRunning(true);

      timeOrigin.current = Date.now();
      intervalId.current = setInterval(() => {
        setElapsed((e) => {
          const baseTime = timeOrigin.current;
          timeOrigin.current = Date.now();
          return e + Date.now() - baseTime;
        });
      }, 50);
    } else {
      // pausing
      setRunning(false);
      clearInterval(intervalId.current);
    }
  };

  const onReset = () => {
    if (running) onPress();
    setElapsed(0);
  };

  const studying: boolean = elapsed % 20000 < 15000;
  const stopped: boolean = elapsed === 0;

  const shown =
    stopped || studying
      ? 15000 - (elapsed % 20000)
      : 5000 - ((elapsed % 20000) - 15000);

  const label = stopped
    ? "Not running!"
    : studying
    ? "Time to work!"
    : "Take a break!";

  useEffect(() => {
    if (label !== "Not running!") Alert.alert(label);
  }, [label]);

  return (
    <View
      style={styles[label === "Time to work!" ? "container" : "container2"]}
    >
      <StatusBar style="auto" />
      <View style={styles.screen}>
        <Text style={styles.labelText}>{label}</Text>
        <Text style={[styles.labelText, styles.timeText]}>
          {new Date(shown).toISOString().substr(17, 5)}
        </Text>
        <View style={styles.buttonRow}>
          <View style={styles.button}>
            <Button title={running ? "Pause" : "Start"} onPress={onPress} />
          </View>
          <View style={styles.button}>
            <Button title="Reset" onPress={onReset} />
          </View>
        </View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "rgb(219, 82, 77)",
  },
  container2: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#89CFF0",
  },
  screen: {
    ...StyleSheet.absoluteFillObject,
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  buttonRow: {
    flexDirection: "row",
    justifyContent: "center",
    marginTop: 10,
  },
  labelText: {
    fontSize: 30,
    color: "white",
    fontWeight: "bold",
  },
  timeText: {
    fontSize: 120,
    fontWeight: "400",
  },
  button: {
    marginLeft: 5,
    marginRight: 5,
  },
});
