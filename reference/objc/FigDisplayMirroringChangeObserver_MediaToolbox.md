# `FigDisplayMirroringChangeObserver`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 1 properties, 11 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigPlayer=} _player;
@"NSMutableSet" _clonedDisplays;
@"NSMutableSet" _cloningSupportedDisplays;
@"NSArray" _baseDisplayList;
B _needToRemoveObserversOnCADisplays;
^? _callback;
^{OpaqueFigCFWeakReferenceHolder=} _weakCallbackContext;
```

## Properties

```
@property (T@"NSArray",&,N) baseDisplayList;
```

## Instance methods

```
-[FigDisplayMirroringChangeObserver baseDisplayList];
-[FigDisplayMirroringChangeObserver observeValueForKeyPath:ofObject:change:context:];
-[FigDisplayMirroringChangeObserver init];
-[FigDisplayMirroringChangeObserver removeObserversOnCADisplays];
-[FigDisplayMirroringChangeObserver dealloc];
-[FigDisplayMirroringChangeObserver initWithPlayer:];
-[FigDisplayMirroringChangeObserver removeCallback];
-[FigDisplayMirroringChangeObserver removeReferenceToPlayer];
-[FigDisplayMirroringChangeObserver initWithCallback:context:];
-[FigDisplayMirroringChangeObserver setBaseDisplayList:];
-[FigDisplayMirroringChangeObserver updatePlayerDisplayList];
```
