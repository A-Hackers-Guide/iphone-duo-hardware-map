# `SBSystemActionElementPreviewing` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 9 instance methods, 0 class methods

## Properties

```
@property (TB,N,GisPreviewing) previewing;
@property (TB,N,GisUrgent) urgent;
@property (TB,N,GisExpanding) expanding;
@property (TB,N,GisProminent) prominent;
```

## Instance methods

```
-[SBSystemActionElementPreviewing pop];
-[SBSystemActionElementPreviewing isUrgent];
-[SBSystemActionElementPreviewing setUrgent:];
-[SBSystemActionElementPreviewing setProminent:];
-[SBSystemActionElementPreviewing isProminent];
-[SBSystemActionElementPreviewing isPreviewing];
-[SBSystemActionElementPreviewing setPreviewing:];
-[SBSystemActionElementPreviewing isExpanding];
-[SBSystemActionElementPreviewing setExpanding:];
```
