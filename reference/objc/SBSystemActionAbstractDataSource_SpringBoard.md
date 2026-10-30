# `SBSystemActionAbstractDataSource`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemActionDataSource`
- 3 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"NSString" _hostIdentifier;
@"SBSystemAction" _selectedSystemAction;
```

## Properties

```
@property (T@"SBSystemAction",&,N,V_selectedSystemAction) selectedSystemAction;
@property (T@"NSString",R,C,N,V_hostIdentifier) hostIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemActionAbstractDataSource hostIdentifier];
-[SBSystemActionAbstractDataSource removeObserver:];
-[SBSystemActionAbstractDataSource addObserver:];
-[SBSystemActionAbstractDataSource initWithHostIdentifier:];
-[SBSystemActionAbstractDataSource setSelectedSystemAction:];
-[SBSystemActionAbstractDataSource executorForSystemAction:];
-[SBSystemActionAbstractDataSource selectedSystemAction];
-[SBSystemActionAbstractDataSource updateSelectedAction];
```
