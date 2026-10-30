# `SBFHingeSamples`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 8 instance methods, 3 class methods

## Instance variables

```
@"NSArray" _loops;
```

## Properties

```
@property (T@"NSArray",R,N,V_loops) loops;
```

## Class methods

```
+[SBFHingeSamples defaultPath];
+[SBFHingeSamples allowsCallerSuppliedPath];
+[SBFHingeSamples samplesWithContentsOfFile:error:];
```

## Instance methods

```
-[SBFHingeSamples loops];
-[SBFHingeSamples _parseDirective:identifier:band:direction:];
-[SBFHingeSamples _parseSample:into:];
-[SBFHingeSamples _sweepFromPending:direction:];
-[SBFHingeSamples initWithText:path:error:];
-[SBFHingeSamples loopWithIdentifier:];
-[SBFHingeSamples loopsInBand:];
-[SBFHingeSamples randomLoopInBand:seed:];
```
