# `CBAODFlipBookWrapper`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _flipBookData;
d _submissionTimestamp;
{?="version"C"sizeOfHeader"I"sizeOfEntry"I"numberOfUpdates"I"frequency"S"length"f"ambient"f} _header;
{?="brightness"f"brightnessLimit"f"pccFactor"f"twilightStrength"f"twilightLux"f"ammoliteStrength"f"ammoliteLux"f"whitepoint"{?="matrix"[3[3f]]"xy"{?="x"f"y"f}"Y"f}} _origin;
```

## Properties

```
@property (T{?=CIIISff},R,N,V_header) header;
@property (T{?=fffffff{?=[3[3f]]{?=ff}f}},R,N,V_origin) origin;
@property (TQ,R,N) entryCount;
@property (Td,N,V_submissionTimestamp) submissionTimestamp;
```

## Instance methods

```
-[CBAODFlipBookWrapper header];
-[CBAODFlipBookWrapper origin];
-[CBAODFlipBookWrapper dealloc];
-[CBAODFlipBookWrapper description];
-[CBAODFlipBookWrapper entryCount];
-[CBAODFlipBookWrapper getEntry:forID:];
-[CBAODFlipBookWrapper isValidEntryID:];
-[CBAODFlipBookWrapper newFlipBookData];
-[CBAODFlipBookWrapper appendFlipBookEntry:];
-[CBAODFlipBookWrapper initWithHeader:andOrigin:];
-[CBAODFlipBookWrapper setSubmissionTimestamp:];
-[CBAODFlipBookWrapper submissionTimestamp];
```
