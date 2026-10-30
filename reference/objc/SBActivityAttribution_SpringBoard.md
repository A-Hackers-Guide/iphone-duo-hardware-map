# `SBActivityAttribution`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `BSDescriptionProviding`
- 4 instance variables, 13 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"STActivityAttribution" _attribution;
B _isSystemExecutable;
i _pid;
@"NSString" _attributionGroup;
```

## Properties

```
@property (Ti,R,N,V_pid) pid;
@property (T{?=[8I]},R,N) auditToken;
@property (T@"NSString",R,C,N) bundleIdentifier;
@property (T@"NSString",R,C,N) displayName;
@property (T@"NSString",R,C,N) executableDisplayName;
@property (T@"NSString",R,C,N,V_attributionGroup) attributionGroup;
@property (T@"NSString",R,C,N) website;
@property (TB,R,N) isSystemService;
@property (T@"NSString",R,C,N) activeEntityBundleIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBActivityAttribution website];
-[SBActivityAttribution succinctDescriptionBuilder];
-[SBActivityAttribution displayName];
-[SBActivityAttribution bundleIdentifier];
-[SBActivityAttribution descriptionWithMultilinePrefix:];
-[SBActivityAttribution succinctDescription];
-[SBActivityAttribution pid];
-[SBActivityAttribution hash];
-[SBActivityAttribution description];
-[SBActivityAttribution auditToken];
-[SBActivityAttribution isSystemService];
-[SBActivityAttribution copyWithZone:];
-[SBActivityAttribution isEqual:];
-[SBActivityAttribution descriptionBuilderWithMultilinePrefix:];
-[SBActivityAttribution _activityAttribution];
-[SBActivityAttribution activeEntityBundleIdentifier];
-[SBActivityAttribution attributionGroup];
-[SBActivityAttribution executableDisplayName];
-[SBActivityAttribution hasMatchingAttributedEntity:];
-[SBActivityAttribution initWithSTActivityAttribution:];
```
