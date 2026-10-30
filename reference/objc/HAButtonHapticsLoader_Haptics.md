# `HAButtonHapticsLoader`

- Image: [`/System/Library/PrivateFrameworks/Haptics.framework/Haptics`](../userland/System__Library__PrivateFrameworks__Haptics.framework__Haptics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 2 properties, 10 instance methods, 1 class methods

## Properties

```
@property (Tq,R,N) maxNumberOfSlots;
@property (TB,R,N) serviceAvailable;
```

## Class methods

```
+[HAButtonHapticsLoader sharedInstance];
```

## Instance methods

```
-[HAButtonHapticsLoader dealloc];
-[HAButtonHapticsLoader hapticAssetType:hasAudio:hasHaptic:error:];
-[HAButtonHapticsLoader loadButtonHapticOfType:withParameters:atSlot:error:];
-[HAButtonHapticsLoader maxNumberOfSlots];
-[HAButtonHapticsLoader serviceAvailable];
-[HAButtonHapticsLoader audioGainForType:];
-[HAButtonHapticsLoader defaultDownGainForType:];
-[HAButtonHapticsLoader defaultUpGainForType:];
-[HAButtonHapticsLoader hapticGainForType:];
-[HAButtonHapticsLoader loadButtonHapticOfType:atSlot:error:];
```
