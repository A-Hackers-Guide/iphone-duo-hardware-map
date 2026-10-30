# `SBIconProfileModelMemoryStore`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBIconModelStore`
- 2 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _currentState;
@"NSDictionary" _desiredState;
```

## Properties

```
@property (T@"NSDictionary",C,N,V_currentState) currentState;
@property (T@"NSDictionary",C,N,V_desiredState) desiredState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBIconProfileModelMemoryStore init];
-[SBIconProfileModelMemoryStore setCurrentState:];
-[SBIconProfileModelMemoryStore currentState];
-[SBIconProfileModelMemoryStore desiredState];
-[SBIconProfileModelMemoryStore deleteCurrentIconStateWithOptions:error:];
-[SBIconProfileModelMemoryStore deleteDesiredIconStateWithOptions:error:];
-[SBIconProfileModelMemoryStore loadCurrentIconState:];
-[SBIconProfileModelMemoryStore loadDesiredIconState:];
-[SBIconProfileModelMemoryStore saveCurrentIconState:error:];
-[SBIconProfileModelMemoryStore saveDesiredIconState:error:];
-[SBIconProfileModelMemoryStore initWithCurrentState:desiredState:];
-[SBIconProfileModelMemoryStore setDesiredState:];
-[SBIconProfileModelMemoryStore initWithITunesRepresentation:];
```
