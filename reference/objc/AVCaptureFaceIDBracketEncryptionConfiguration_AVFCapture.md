# `AVCaptureFaceIDBracketEncryptionConfiguration`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
Q _hostMainKeyIndex;
@"NSData" _nonce;
@"NSData" _initializationVector;
@"NSData" _linearFeedbackShiftRegisterSeed;
```

## Properties

```
@property (T@"NSDictionary",R,N) faceIDBracketEncryptionConfigurationDictionary;
@property (TQ,N,V_hostMainKeyIndex) hostMainKeyIndex;
@property (T@"NSData",&,N,V_nonce) nonce;
@property (T@"NSData",&,N,V_initializationVector) initializationVector;
@property (T@"NSData",&,N,V_linearFeedbackShiftRegisterSeed) linearFeedbackShiftRegisterSeed;
```

## Instance methods

```
-[AVCaptureFaceIDBracketEncryptionConfiguration nonce];
-[AVCaptureFaceIDBracketEncryptionConfiguration setInitializationVector:];
-[AVCaptureFaceIDBracketEncryptionConfiguration dealloc];
-[AVCaptureFaceIDBracketEncryptionConfiguration initializationVector];
-[AVCaptureFaceIDBracketEncryptionConfiguration copyWithZone:];
-[AVCaptureFaceIDBracketEncryptionConfiguration isEqual:];
-[AVCaptureFaceIDBracketEncryptionConfiguration setNonce:];
-[AVCaptureFaceIDBracketEncryptionConfiguration linearFeedbackShiftRegisterSeed];
-[AVCaptureFaceIDBracketEncryptionConfiguration faceIDBracketEncryptionConfigurationDictionary];
-[AVCaptureFaceIDBracketEncryptionConfiguration hostMainKeyIndex];
-[AVCaptureFaceIDBracketEncryptionConfiguration setHostMainKeyIndex:];
-[AVCaptureFaceIDBracketEncryptionConfiguration setLinearFeedbackShiftRegisterSeed:];
```
