# `SBDisplayItemLayoutAttributes`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `BSDescriptionProviding`
- 16 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
Q _hash;
B _cascaded;
B _positionIsSystemManaged;
q _contentOrientation;
q _lastInteractionTime;
q _sizingPolicy;
q _version;
q _occlusionState;
{SBDisplayItemSplitConfiguration="splitRole"q"isActive"B} _splitConfiguration;
{?="uuidBytes"[16C]} _splitIdentifier;
{CGPoint="x"d"y"d} _normalizedCenter;
{CGPoint="x"d"y"d} _unoccludedPeekingCenter;
{SBDisplayItemTileConfiguration="tileRole"q"customSize"{CGSize="width"d"height"d}} _tileConfiguration;
{SBDisplayItemSlideOverConfiguration="corner"q"yOffsetFromCorner"d"size"{CGSize="width"d"height"d}"isActive"B"isStashed"B"dodgesDock"B} _slideOverConfiguration;
{SBDisplayItemAttributedSize="_private_opaqueSize"{CGSize="width"d"height"d}"referenceBounds"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"semanticSizeType"q} _attributedSize;
{SBDisplayItemAttributedSize="_private_opaqueSize"{CGSize="width"d"height"d}"referenceBounds"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"semanticSizeType"q} _attributedUserSizeBeforeOverlapping;
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
-[SBDisplayItemLayoutAttributes debugDescription];
-[SBDisplayItemLayoutAttributes succinctDescriptionBuilder];
-[SBDisplayItemLayoutAttributes init];
-[SBDisplayItemLayoutAttributes descriptionWithMultilinePrefix:];
-[SBDisplayItemLayoutAttributes succinctDescription];
-[SBDisplayItemLayoutAttributes hash];
-[SBDisplayItemLayoutAttributes description];
-[SBDisplayItemLayoutAttributes copyWithZone:];
-[SBDisplayItemLayoutAttributes isEqual:];
-[SBDisplayItemLayoutAttributes descriptionBuilderWithMultilinePrefix:];
-[SBDisplayItemLayoutAttributes _appendPropertiesToBuilder:];
-[SBDisplayItemLayoutAttributes _initWithContentOrientation:lastInteractionTime:sizingPolicy:attributedSize:tileConfiguration:slideOverConfiguration:splitConfiguration:normalizedCenter:cascaded:occlusionState:attributedUserSizeBeforeOverlapping:unoccludedPeekingCenter:positionIsSystemManaged:splitIdentifier:version:];
-[SBDisplayItemLayoutAttributes _sizeForAttributedSize:inBounds:defaultSize:screenEdgePadding:];
-[SBDisplayItemLayoutAttributes sb_isDisplayItemLayoutAttributes];
```
