# `MTLDebugLocation`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"MTLDebugInstrumentationData" _data;
^{DebugLocation=IIII} _debugLoc;
```

## Properties

```
@property (T@"MTLDebugSubProgram",R,N) scope;
@property (TI,R,N) line;
@property (TI,R,N) column;
@property (T@"MTLDebugLocation",R,N) inlinedAt;
```

## Instance methods

```
-[MTLDebugLocation scope];
-[MTLDebugLocation formattedDescription:];
-[MTLDebugLocation dealloc];
-[MTLDebugLocation retain];
-[MTLDebugLocation release];
-[MTLDebugLocation description];
-[MTLDebugLocation column];
-[MTLDebugLocation line];
-[MTLDebugLocation releaseInternal];
-[MTLDebugLocation inlinedAt];
```
