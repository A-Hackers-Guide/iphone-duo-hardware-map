# `CBLEAudioPeripheralUpdateEvent`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
q _eventType;
@"NSString" _includedServiceDescription;
@"NSNumber" _updatedValue;
@"NSError" _error;
```

## Properties

```
@property (Tq,R,N,V_eventType) eventType;
@property (T@"NSString",R,C,N,V_includedServiceDescription) includedServiceDescription;
@property (T@"NSNumber",R,C,N,V_updatedValue) updatedValue;
@property (T@"NSError",R,C,N,V_error) error;
```

## Instance methods

```
-[CBLEAudioPeripheralUpdateEvent eventType];
-[CBLEAudioPeripheralUpdateEvent error];
-[CBLEAudioPeripheralUpdateEvent initWithEventType:];
-[CBLEAudioPeripheralUpdateEvent updatedValue];
-[CBLEAudioPeripheralUpdateEvent includedServiceDescription];
-[CBLEAudioPeripheralUpdateEvent initWithError:withError:];
-[CBLEAudioPeripheralUpdateEvent initWithValue:withValue:];
-[CBLEAudioPeripheralUpdateEvent setOptionalIncludedServiceDescription:];
```
