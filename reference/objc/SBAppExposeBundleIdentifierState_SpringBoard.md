# `SBAppExposeBundleIdentifierState`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`
- 2 instance variables, 8 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSString" _leadingBundleID;
@"NSString" _trailingBundleID;
```

## Properties

```
@property (T@"NSString",R,C,N,V_leadingBundleID) leadingBundleID;
@property (T@"NSString",R,C,N,V_trailingBundleID) trailingBundleID;
@property (T@"NSString",R,C,N) effectiveBundleID;
@property (TB,R,N) isFullScreen;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBAppExposeBundleIdentifierState stateWithFullScreenBundleID:];
```

## Instance methods

```
-[SBAppExposeBundleIdentifierState isFullScreen];
-[SBAppExposeBundleIdentifierState effectiveBundleID];
-[SBAppExposeBundleIdentifierState hash];
-[SBAppExposeBundleIdentifierState description];
-[SBAppExposeBundleIdentifierState appendDescriptionToStream:];
-[SBAppExposeBundleIdentifierState isEqual:];
-[SBAppExposeBundleIdentifierState leadingBundleID];
-[SBAppExposeBundleIdentifierState initWithLeadingBundleID:trailingBundleID:];
-[SBAppExposeBundleIdentifierState stateByMergingWithPreviousState:];
-[SBAppExposeBundleIdentifierState trailingBundleID];
```
