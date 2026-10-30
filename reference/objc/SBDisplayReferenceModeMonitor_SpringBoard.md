# `SBDisplayReferenceModeMonitor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _displayToCachedStatus;
@"NSMutableDictionary" _CADisplayIdentifierToObservers;
@"NSMutableDictionary" _CADisplayIdentifierToFBSDisplayConfig;
@"NSMutableSet" _observedDisplays;
```

## Class methods

```
+[SBDisplayReferenceModeMonitor canAddObserverForDisplayWithConfiguration:];
```

## Instance methods

```
-[SBDisplayReferenceModeMonitor observeValueForKeyPath:ofObject:change:context:];
-[SBDisplayReferenceModeMonitor dealloc];
-[SBDisplayReferenceModeMonitor _startObservingDisplayIfNeeded:];
-[SBDisplayReferenceModeMonitor _referenceModeStatusForDisplay:];
-[SBDisplayReferenceModeMonitor _addObserver:forDisplay:];
-[SBDisplayReferenceModeMonitor _cachedStatusForDisplay:];
-[SBDisplayReferenceModeMonitor _configurationForDisplay:];
-[SBDisplayReferenceModeMonitor _displayForConfiguration:];
-[SBDisplayReferenceModeMonitor _enumerateObserversOfDisplay:usingBlock:];
-[SBDisplayReferenceModeMonitor _observersForDisplay:];
-[SBDisplayReferenceModeMonitor _removeCachedStatusForDisplay:];
-[SBDisplayReferenceModeMonitor _removeObserver:forDisplay:];
-[SBDisplayReferenceModeMonitor _setCachedStatus:forDisplay:];
-[SBDisplayReferenceModeMonitor _setConfig:forDisplay:];
-[SBDisplayReferenceModeMonitor _shouldNotifyObserversOfReferenceModeStatusChangeForDisplay:];
-[SBDisplayReferenceModeMonitor _stopObservingDisplay:];
-[SBDisplayReferenceModeMonitor addReferenceModeStatusObserver:forDisplayWithConfiguration:];
-[SBDisplayReferenceModeMonitor referenceModeStatusForDisplayWithConfiguration:];
-[SBDisplayReferenceModeMonitor removeReferenceModeStatusObserver:forDisplayWithConfiguration:];
```
