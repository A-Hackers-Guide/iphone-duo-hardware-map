# `HIDDisplayPresetData`

- Image: [`/System/Library/PrivateFrameworks/HIDDisplay.framework/HIDDisplay`](../userland/System__Library__PrivateFrameworks__HIDDisplay.framework__HIDDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
q _index;
@"HIDDisplayPresetInterface" _deviceRef;
```

## Properties

```
@property (TB,R) valid;
@property (TB,R) writable;
@property (T@"NSData",R) uniqueID;
```

## Instance methods

```
-[HIDDisplayPresetData valid];
-[HIDDisplayPresetData uniqueID];
-[HIDDisplayPresetData writable];
-[HIDDisplayPresetData get:];
-[HIDDisplayPresetData hidDisplay];
-[HIDDisplayPresetData initWithDisplayDevice:index:];
-[HIDDisplayPresetData set:error:];
-[HIDDisplayPresetData setHidDisplay:];
```
