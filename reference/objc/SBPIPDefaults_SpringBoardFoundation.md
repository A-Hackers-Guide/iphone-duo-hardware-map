# `SBPIPDefaults`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAbstractSpringBoardDefaultDomain`
- 0 instance variables, 6 properties, 5 instance methods, 0 class methods

## Properties

```
@property (T@"NSDictionary",D,N) lastKnownCornerPositionByContentType;
@property (T@"NSDictionary",D,N) lastKnownSizeByContentType;
@property (TB,R,D,N) allowAutoPIP;
@property (TB,R,D,N) visualizeKeyboardFrame;
@property (TB,R,D,N) visualizePositionRegions;
@property (TB,D,N) initiallyUsesMinimumPreferredContentSize;
```

## Instance methods

```
-[SBPIPDefaults _bindAndRegisterDefaults];
-[SBPIPDefaults lastKnownCornerPositionForContentType:];
-[SBPIPDefaults lastKnownSizeForContentType:];
-[SBPIPDefaults setLastKnownCornerPosition:contentType:];
-[SBPIPDefaults setLastKnownSize:contentType:];
```
