# `SBDisplayItemLayoutAttributesStorage`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 2 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _layoutAttributesMap;
@"NSMapTable" _cachedKeySets;
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
-[SBDisplayItemLayoutAttributesStorage succinctDescriptionBuilder];
-[SBDisplayItemLayoutAttributesStorage init];
-[SBDisplayItemLayoutAttributesStorage descriptionWithMultilinePrefix:];
-[SBDisplayItemLayoutAttributesStorage succinctDescription];
-[SBDisplayItemLayoutAttributesStorage layoutAttributesMap];
-[SBDisplayItemLayoutAttributesStorage description];
-[SBDisplayItemLayoutAttributesStorage descriptionBuilderWithMultilinePrefix:];
-[SBDisplayItemLayoutAttributesStorage bestEffortLayoutAttributesForKey:];
-[SBDisplayItemLayoutAttributesStorage enumarateLayoutAttributesForDisplayItem:block:];
-[SBDisplayItemLayoutAttributesStorage lasInteractionTimeForDisplayItem:];
-[SBDisplayItemLayoutAttributesStorage layoutAttributesForKey:];
-[SBDisplayItemLayoutAttributesStorage setLayoutAttributes:forKey:];
-[SBDisplayItemLayoutAttributesStorage updateEntriesWithBlock:];
```
