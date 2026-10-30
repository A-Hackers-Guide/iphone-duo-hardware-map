# `MTLDebugInstrumentationData`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_data>" _dataMap;
r^v _data;
{vector<const __CFString *, std::allocator<const __CFString *>>="__begin_"^^{__CFString}"__end_"^^{__CFString}""{?="__cap_"^^{__CFString}}} _strings;
{vector<MTLDebugLocation *, std::allocator<MTLDebugLocation *>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} _debugLocations;
{vector<MTLDebugSubProgram *, std::allocator<MTLDebugSubProgram *>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} _debugSubPrograms;
@"NSData" _globalConstantsData;
@"NSObject<OS_dispatch_data>" _userReflectionData;
@"NSArray" _linkedDynamicLibraries;
```

## Properties

```
@property (TB,R,N) hasGlobalConstantsInstrumentationFailures;
@property (TB,R,N) hasArgumentBufferInstrumentationFailures;
@property (TB,R,N) hasArgumentLimitsInstrumentationFailures;
@property (TI,R,N) threadgroupArgumentOffset;
@property (TI,R,N) activeThreadgroupMask;
@property (TQ,R,N) bufferAccessMask;
```

## Instance methods

```
-[MTLDebugInstrumentationData dealloc];
-[MTLDebugInstrumentationData initWithData:];
-[MTLDebugInstrumentationData activeThreadgroupMask];
-[MTLDebugInstrumentationData bufferAccessMask];
-[MTLDebugInstrumentationData debugLocationForID:];
-[MTLDebugInstrumentationData debugSubProgramForID:];
-[MTLDebugInstrumentationData globalConstantsData];
-[MTLDebugInstrumentationData hasArgumentBufferInstrumentationFailures];
-[MTLDebugInstrumentationData hasArgumentLimitsInstrumentationFailures];
-[MTLDebugInstrumentationData hasGlobalConstantsInstrumentationFailures];
-[MTLDebugInstrumentationData initWithData:linkedDynamicLibraries:];
-[MTLDebugInstrumentationData linkedDynamicLibraries];
-[MTLDebugInstrumentationData releaseLinkedDynamicLibraries];
-[MTLDebugInstrumentationData stringForID:];
-[MTLDebugInstrumentationData threadgroupArgumentOffset];
-[MTLDebugInstrumentationData userReflectionData];
```
