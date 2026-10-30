# `SBFocusAppConfigurationContextMonitor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DNDModeConfigurationServiceListener`
- 4 instance variables, 4 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSDictionary" _lock_prefixes;
@"DNDModeConfigurationService" _configurationService;
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
+[SBFocusAppConfigurationContextMonitor sharedInstance];
```

## Instance methods

```
-[SBFocusAppConfigurationContextMonitor init];
-[SBFocusAppConfigurationContextMonitor modeConfigurationService:didReceiveAppConfigurationContextUpdateForModeIdentifier:];
-[SBFocusAppConfigurationContextMonitor _updatePrefixes:];
-[SBFocusAppConfigurationContextMonitor targetContentIdentifierPrefixForBundleIdentifier:];
```
