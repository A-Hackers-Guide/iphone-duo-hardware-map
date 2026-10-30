# `AMSBTLEPeripheral`

- Image: [`/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit`](../userland/System__Library__Frameworks__CoreAudioKit.framework__CoreAudioKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 9 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"CBPeripheral" peripheral;
@"NSString" uuid;
@"NSString" name;
@"CBCentralManager" centralManager;
d lastSeen;
B inputAvailable;
B outputAvailable;
B online;
B available;
B changingState;
```

## Properties

```
@property (T@"CBPeripheral",R) peripheral;
@property (T@"NSString",R,&) uuid;
@property (T@"NSString",&) name;
@property (Td) lastSeen;
@property (TB) inputAvailable;
@property (TB) outputAvailable;
@property (TB,GisOnline) online;
@property (TB,GisChangingState,VchangingState) changingState;
@property (TB,GisAvailable) available;
```

## Instance methods

```
-[AMSBTLEPeripheral connect];
-[AMSBTLEPeripheral isOnline];
-[AMSBTLEPeripheral isAvailable];
-[AMSBTLEPeripheral setOnline:];
-[AMSBTLEPeripheral uuid];
-[AMSBTLEPeripheral dealloc];
-[AMSBTLEPeripheral isChangingState];
-[AMSBTLEPeripheral setAvailable:];
-[AMSBTLEPeripheral lastSeen];
-[AMSBTLEPeripheral disconnect];
-[AMSBTLEPeripheral setLastSeen:];
-[AMSBTLEPeripheral setName:];
-[AMSBTLEPeripheral name];
-[AMSBTLEPeripheral hidden];
-[AMSBTLEPeripheral peripheral];
-[AMSBTLEPeripheral outputAvailable];
-[AMSBTLEPeripheral inputAvailable];
-[AMSBTLEPeripheral setInputAvailable:];
-[AMSBTLEPeripheral setOutputAvailable:];
-[AMSBTLEPeripheral canConnect];
-[AMSBTLEPeripheral initWithID:name:manager:];
-[AMSBTLEPeripheral setChangingState:];
-[AMSBTLEPeripheral updateAvailableStateChanged];
```
