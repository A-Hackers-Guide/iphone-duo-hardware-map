# `SBPressSequenceSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 20 instance methods, 0 class methods

## Instance variables

```
Q _numberOfPresses;
d _maxDefaultPressDownDuration;
d _maxDefaultPressUpDuration;
d _maxDownToDownDuration;
Q _indexOfPressDownToUseForVarianceAndGrowth;
Q _numberOfPressDownGrowthTerms;
Q _indexOfPressUpToUseForVarianceAndGrowth;
Q _numberOfPressUpGrowthTerms;
d _pressDownVariance;
d _pressUpVariance;
```

## Properties

```
@property (TQ,N,V_numberOfPresses) numberOfPresses;
@property (Td,N,V_maxDefaultPressDownDuration) maxDefaultPressDownDuration;
@property (Td,N,V_maxDefaultPressUpDuration) maxDefaultPressUpDuration;
@property (Td,N,V_maxDownToDownDuration) maxDownToDownDuration;
@property (TQ,N,V_indexOfPressDownToUseForVarianceAndGrowth) indexOfPressDownToUseForVarianceAndGrowth;
@property (TQ,N,V_numberOfPressDownGrowthTerms) numberOfPressDownGrowthTerms;
@property (TQ,N,V_indexOfPressUpToUseForVarianceAndGrowth) indexOfPressUpToUseForVarianceAndGrowth;
@property (TQ,N,V_numberOfPressUpGrowthTerms) numberOfPressUpGrowthTerms;
@property (Td,N,V_pressDownVariance) pressDownVariance;
@property (Td,N,V_pressUpVariance) pressUpVariance;
```

## Instance methods

```
-[SBPressSequenceSettings pressUpVariance];
-[SBPressSequenceSettings numberOfPresses];
-[SBPressSequenceSettings setMaxDefaultPressDownDuration:];
-[SBPressSequenceSettings indexOfPressDownToUseForVarianceAndGrowth];
-[SBPressSequenceSettings indexOfPressUpToUseForVarianceAndGrowth];
-[SBPressSequenceSettings maxDefaultPressDownDuration];
-[SBPressSequenceSettings maxDefaultPressUpDuration];
-[SBPressSequenceSettings maxDownToDownDuration];
-[SBPressSequenceSettings numberOfPressDownGrowthTerms];
-[SBPressSequenceSettings numberOfPressUpGrowthTerms];
-[SBPressSequenceSettings pressDownVariance];
-[SBPressSequenceSettings setIndexOfPressDownToUseForVarianceAndGrowth:];
-[SBPressSequenceSettings setIndexOfPressUpToUseForVarianceAndGrowth:];
-[SBPressSequenceSettings setMaxDefaultPressUpDuration:];
-[SBPressSequenceSettings setMaxDownToDownDuration:];
-[SBPressSequenceSettings setNumberOfPressDownGrowthTerms:];
-[SBPressSequenceSettings setNumberOfPressUpGrowthTerms:];
-[SBPressSequenceSettings setNumberOfPresses:];
-[SBPressSequenceSettings setPressDownVariance:];
-[SBPressSequenceSettings setPressUpVariance:];
```
