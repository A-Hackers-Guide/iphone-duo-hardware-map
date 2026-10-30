# `AVCaptureFaceIDBracketConfiguration`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 6 instance variables, 7 properties, 17 instance methods, 0 class methods

## Instance variables

```
Q _numberOfDoubles;
@"NSArray" _doubleOrder;
Q _probePatternType;
Q _probePatternIndex;
@"AVCaptureFaceIDBracketEncryptionConfiguration" _colorBracketEncryptionConfiguration;
@"AVCaptureFaceIDBracketEncryptionConfiguration" _infraredBracketEncryptionConfiguration;
```

## Properties

```
@property (T@"NSDictionary",R,N) faceIDBracketConfigurationDictionary;
@property (TQ,N,V_numberOfDoubles) numberOfDoubles;
@property (T@"NSArray",C,N,V_doubleOrder) doubleOrder;
@property (TQ,N,V_probePatternType) probePatternType;
@property (TQ,N,V_probePatternIndex) probePatternIndex;
@property (T@"AVCaptureFaceIDBracketEncryptionConfiguration",C,N,V_colorBracketEncryptionConfiguration) colorBracketEncryptionConfiguration;
@property (T@"AVCaptureFaceIDBracketEncryptionConfiguration",C,N,V_infraredBracketEncryptionConfiguration) infraredBracketEncryptionConfiguration;
```

## Instance methods

```
-[AVCaptureFaceIDBracketConfiguration init];
-[AVCaptureFaceIDBracketConfiguration dealloc];
-[AVCaptureFaceIDBracketConfiguration copyWithZone:];
-[AVCaptureFaceIDBracketConfiguration isEqual:];
-[AVCaptureFaceIDBracketConfiguration numberOfDoubles];
-[AVCaptureFaceIDBracketConfiguration setDoubleOrder:];
-[AVCaptureFaceIDBracketConfiguration colorBracketEncryptionConfiguration];
-[AVCaptureFaceIDBracketConfiguration doubleOrder];
-[AVCaptureFaceIDBracketConfiguration faceIDBracketConfigurationDictionary];
-[AVCaptureFaceIDBracketConfiguration infraredBracketEncryptionConfiguration];
-[AVCaptureFaceIDBracketConfiguration probePatternIndex];
-[AVCaptureFaceIDBracketConfiguration probePatternType];
-[AVCaptureFaceIDBracketConfiguration setColorBracketEncryptionConfiguration:];
-[AVCaptureFaceIDBracketConfiguration setInfraredBracketEncryptionConfiguration:];
-[AVCaptureFaceIDBracketConfiguration setNumberOfDoubles:];
-[AVCaptureFaceIDBracketConfiguration setProbePatternIndex:];
-[AVCaptureFaceIDBracketConfiguration setProbePatternType:];
```
