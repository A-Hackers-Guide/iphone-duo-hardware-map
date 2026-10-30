# `SBVoiceControlPresentationSource`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 3 instance methods, 3 class methods

## Instance variables

```
@"BluetoothDevice" _bluetoothDevice;
q _sourceType;
```

## Properties

```
@property (Tq,R,N,V_sourceType) sourceType;
@property (T@"BluetoothDevice",R,N,V_bluetoothDevice) bluetoothDevice;
```

## Class methods

```
+[SBVoiceControlPresentationSource sourceFromBluetoothDevice:];
+[SBVoiceControlPresentationSource sourceFromHeadsetButton];
+[SBVoiceControlPresentationSource sourceFromHomeButton];
```

## Instance methods

```
-[SBVoiceControlPresentationSource sourceType];
-[SBVoiceControlPresentationSource bluetoothDevice];
-[SBVoiceControlPresentationSource _initWithSourceType:];
```
