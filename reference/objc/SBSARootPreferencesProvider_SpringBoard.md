# `SBSARootPreferencesProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSABasePreferencesProvider`
- Protocols: `SBSAStackablePreferencesProviding`
- 4 instance variables, 6 properties, 10 instance methods, 1 class methods

## Instance variables

```
B _configuredInitialStack;
@"NSArray" _previouslyVisibleElements;
{?="interfaceOrientation"q"layoutDirection"q"statusBarAxis"q"sensorVariant"Q} _previousOrientationEnvironment;
@"SBSAElementLayoutTransition" _lastChangingElementLayoutTransition;
```

## Properties

```
@property (T@"<SBSAStackablePreferencesProviding>",R,W,N) parentProvider;
@property (T@"<SBSAStackablePreferencesProviding>",&,N) childProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSARootPreferencesProvider initialize];
```

## Instance methods

```
-[SBSARootPreferencesProvider membersForCoder];
-[SBSARootPreferencesProvider _handleBounceRequest:];
-[SBSARootPreferencesProvider _handleEjectRequest:];
-[SBSARootPreferencesProvider _handlePulseRequest:];
-[SBSARootPreferencesProvider _handleRequests:];
-[SBSARootPreferencesProvider _handleShakeRequest:];
-[SBSARootPreferencesProvider _updateDynamicsSessionProviders:];
-[SBSARootPreferencesProvider initWithParentProvider:];
-[SBSARootPreferencesProvider preferencesFromContext:];
-[SBSARootPreferencesProvider removeFromParentProvider];
```
