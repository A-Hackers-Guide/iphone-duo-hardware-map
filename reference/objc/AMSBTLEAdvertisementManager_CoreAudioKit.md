# `AMSBTLEAdvertisementManager`

- Image: [`/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit`](../userland/System__Library__Frameworks__CoreAudioKit.framework__CoreAudioKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBPeripheralManagerDelegate`
- 1 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"CBPeripheralManager" peripheralManager;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AMSBTLEAdvertisementManager peripheralManagerDidUpdateState:];
-[AMSBTLEAdvertisementManager init];
-[AMSBTLEAdvertisementManager dealloc];
-[AMSBTLEAdvertisementManager isAdvertising];
-[AMSBTLEAdvertisementManager peripheralManager:didReceiveReadRequest:];
-[AMSBTLEAdvertisementManager peripheralManagerDidStartAdvertising:error:];
-[AMSBTLEAdvertisementManager advertiseMIDIService];
-[AMSBTLEAdvertisementManager isLECapableHardware];
-[AMSBTLEAdvertisementManager stopAdvertisingMIDIService];
```
