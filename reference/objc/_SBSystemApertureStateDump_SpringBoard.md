# `_SBSystemApertureStateDump`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`
- 5 instance variables, 9 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"SBSAPreferences" _preferences;
@"SBSAContext" _context;
@"SBSARootPreferencesProvider" _rootPreferencesProvider;
@"SBSystemApertureViewController" _host;
@"NSDate" _timestamp;
```

## Properties

```
@property (T@"SBSAPreferences",&,N,V_preferences) preferences;
@property (T@"SBSAContext",&,N,V_context) context;
@property (T@"SBSARootPreferencesProvider",&,N,V_rootPreferencesProvider) rootPreferencesProvider;
@property (T@"SBSystemApertureViewController",&,N,V_host) host;
@property (T@"NSDate",&,N,V_timestamp) timestamp;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_SBSystemApertureStateDump initialize];
```

## Instance methods

```
-[_SBSystemApertureStateDump setHost:];
-[_SBSystemApertureStateDump setTimestamp:];
-[_SBSystemApertureStateDump setPreferences:];
-[_SBSystemApertureStateDump preferences];
-[_SBSystemApertureStateDump timestamp];
-[_SBSystemApertureStateDump setContext:];
-[_SBSystemApertureStateDump encodeWithCoder:];
-[_SBSystemApertureStateDump context];
-[_SBSystemApertureStateDump host];
-[_SBSystemApertureStateDump membersForCoder];
-[_SBSystemApertureStateDump initWithPreferences:context:rootPreferencesProvider:host:timestamp:];
-[_SBSystemApertureStateDump rootPreferencesProvider];
-[_SBSystemApertureStateDump setRootPreferencesProvider:];
```
