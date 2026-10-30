# `_SBDisplayScaleMappingCache`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSDisplayObserving`
- 2 instance variables, 4 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _hardwareIdentifierToMappings;
@"FBDisplayManager" _displayManager;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_SBDisplayScaleMappingCache sharedInstance];
```

## Instance methods

```
-[_SBDisplayScaleMappingCache init];
-[_SBDisplayScaleMappingCache dealloc];
-[_SBDisplayScaleMappingCache displayMonitor:willDisconnectIdentity:];
-[_SBDisplayScaleMappingCache cacheMapping:];
-[_SBDisplayScaleMappingCache mappingForDisplayIdentifier:];
```
