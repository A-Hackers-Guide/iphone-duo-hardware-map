# `SecSFAParsedCollection`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
B _excludedVersion;
@"NSMutableDictionary" _matchingRules;
@"NSMutableDictionary" _allowedEvents;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_matchingRules) matchingRules;
@property (T@"NSMutableDictionary",&,V_allowedEvents) allowedEvents;
@property (TB,V_excludedVersion) excludedVersion;
```

## Instance methods

```
-[SecSFAParsedCollection excludedVersion];
-[SecSFAParsedCollection allowedEvents];
-[SecSFAParsedCollection matchingRules];
-[SecSFAParsedCollection setAllowedEvents:];
-[SecSFAParsedCollection setExcludedVersion:];
-[SecSFAParsedCollection setMatchingRules:];
```
