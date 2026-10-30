# `SBBackgroundAngelKeepAliveHandler`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 7 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSString" _angelJobLabel;
@"NSString" _assertionName;
@"NSString" _assertionDomain;
@"RBSProcessIdentity" _processIdentity;
@"RBSProcessMonitor" _processMonitor;
@"RBSAssertion" _launchGrantAssertion;
@"RBSProcessHandle" _handleLastGrantedBootstrap;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBBackgroundAngelKeepAliveHandler dealloc];
-[SBBackgroundAngelKeepAliveHandler start];
-[SBBackgroundAngelKeepAliveHandler _process:stateDidUpdate:];
-[SBBackgroundAngelKeepAliveHandler invalidate];
-[SBBackgroundAngelKeepAliveHandler _acquireLaunchGrantAssertion];
-[SBBackgroundAngelKeepAliveHandler _startProcessMonitor];
-[SBBackgroundAngelKeepAliveHandler _takeBootstrapAssertion:];
-[SBBackgroundAngelKeepAliveHandler initWithAngelJobLabel:launchGrantAssertionName:launchGrantAssertionDomain:];
```
