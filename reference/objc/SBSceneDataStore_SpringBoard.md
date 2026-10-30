# `SBSceneDataStore`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 3 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSMutableDictionary" _data;
@"NSMutableDictionary" _archivedObjectCache;
@? _handler;
B _invalidated;
```

## Properties

```
@property (T@"NSDictionary",R,N,G_data,V_data) data;
@property (TB,R,N,G_isInvalidated,V_invalidated) invalidated;
@property (T@"NSString",R,C,N,V_identifier) identifier;
```

## Instance methods

```
-[SBSceneDataStore _isInvalidated];
-[SBSceneDataStore identifier];
-[SBSceneDataStore _invalidate];
-[SBSceneDataStore objectForKey:];
-[SBSceneDataStore _data];
-[SBSceneDataStore setObject:forKey:];
-[SBSceneDataStore removeObjectForKey:];
-[SBSceneDataStore removeAllObjects];
-[SBSceneDataStore safeObjectForKey:ofType:];
-[SBSceneDataStore setArchivedObject:forKey:];
-[SBSceneDataStore unarchivedObjectOfClass:forKey:];
-[SBSceneDataStore _initWithIdentifier:data:changeHandler:];
-[SBSceneDataStore _invokeChangeHandler];
```
