# `SBSwitcherShelf`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `SBSwitcherLayoutElementProviding`, `BSDescriptionProviding`
- 4 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSString" _uniqueIdentifier;
@"NSString" _bundleIdentifier;
q _layoutRole;
Q _displayMode;
```

## Properties

```
@property (T@"NSString",R,C,N,V_uniqueIdentifier) uniqueIdentifier;
@property (T@"NSString",R,C,N,V_bundleIdentifier) bundleIdentifier;
@property (Tq,R,N,V_layoutRole) layoutRole;
@property (TQ,R,N,V_displayMode) displayMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSwitcherShelf layoutRole];
-[SBSwitcherShelf succinctDescriptionBuilder];
-[SBSwitcherShelf isAppLayout];
-[SBSwitcherShelf appLayout];
-[SBSwitcherShelf switcherLayoutElementType];
-[SBSwitcherShelf displayMode];
-[SBSwitcherShelf bundleIdentifier];
-[SBSwitcherShelf descriptionWithMultilinePrefix:];
-[SBSwitcherShelf uniqueIdentifier];
-[SBSwitcherShelf succinctDescription];
-[SBSwitcherShelf hash];
-[SBSwitcherShelf description];
-[SBSwitcherShelf copyWithZone:];
-[SBSwitcherShelf isEqual:];
-[SBSwitcherShelf descriptionBuilderWithMultilinePrefix:];
-[SBSwitcherShelf initWithBundleIdentifier:layoutRole:displayMode:];
```
