# `PKPencilDevice`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 6 properties, 17 instance methods, 2 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
d _lastUsedIimestamp;
^{__IOHIDManager=} _stylusHidManager;
B _isConnected;
B _isRollSupported;
B _isRollSupportUnknown;
i _rollSupportState;
d _baseRollAngle;
q _pencilVersion;
```

## Properties

```
@property (Tq,R,N) pencilVersion;
@property (Tq,R,N) pencilVersionForAnalytics;
@property (TB,R,N) isConnected;
@property (TB,N,V_isRollSupported) isRollSupported;
@property (TB,N,V_isRollSupportUnknown) isRollSupportUnknown;
@property (Td,N,V_baseRollAngle) baseRollAngle;
```

## Class methods

```
+[PKPencilDevice activePencil];
+[PKPencilDevice squeezeThreshold];
```

## Instance methods

```
-[PKPencilDevice isConnected];
-[PKPencilDevice init];
-[PKPencilDevice dealloc];
-[PKPencilDevice isRollSupported];
-[PKPencilDevice _setLastUsedTimestamp:];
-[PKPencilDevice _timeIntervalSinceUsedForTimestamp:];
-[PKPencilDevice appSceneDidEnterBackground];
-[PKPencilDevice baseRollAngle];
-[PKPencilDevice checkIfRollIsSupported:];
-[PKPencilDevice isRollSupportUnknown];
-[PKPencilDevice pencilVersion];
-[PKPencilDevice pencilVersionForAnalytics];
-[PKPencilDevice setBaseRollAngle:];
-[PKPencilDevice setIsRollSupportUnknown:];
-[PKPencilDevice setIsRollSupported:];
-[PKPencilDevice tagAsUsed];
-[PKPencilDevice timeIntervalSinceUsed];
```
