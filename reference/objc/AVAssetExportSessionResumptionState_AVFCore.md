# `AVAssetExportSessionResumptionState`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 5 instance methods, 0 class methods

## Instance variables

```
B _isConfigured;
B _isResumingFromPreviousState;
@"NSString" _failureReason;
```

## Properties

```
@property (TB,R,GisResumptionConfigured) resumptionConfigured;
@property (TB,R,GisResumingFromPreviousState) resumingFromPreviousState;
@property (T@"NSString",R) configurationFailureReason;
```

## Instance methods

```
-[AVAssetExportSessionResumptionState configurationFailureReason];
-[AVAssetExportSessionResumptionState initFailureWithReason:];
-[AVAssetExportSessionResumptionState initSuccessWithIsResuming:];
-[AVAssetExportSessionResumptionState isResumingFromPreviousState];
-[AVAssetExportSessionResumptionState isResumptionConfigured];
```
