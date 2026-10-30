# `SBPBAppLayout`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 21 instance variables, 0 properties, 19 instance methods, 0 class methods

## Instance variables

```
q _preferredDisplayOrdinal;
d _relativeHeight;
d _relativeWidth;
i _centerConfiguration;
@"SBPBDisplayItem" _centerDisplayItem;
i _centerDisplayItemRole;
@"SBPBDisplayItemLayoutAttributes" _centerLayoutAttributes;
@"NSString" _continuousExposeIdentifier;
@"NSMutableArray" _displayItemLayoutAttributes;
@"NSMutableArray" _displayItemLayoutAttributesForNonPreferredDisplays;
@"NSMutableArray" _displayItems;
i _environment;
@"NSMutableArray" _layoutAttributesEntries;
i _layoutConfiguration;
@"SBPBDisplayItem" _primaryDisplayItem;
@"SBPBDisplayItemLayoutAttributes" _primaryLayoutAttributes;
@"SBPBDisplayItem" _secondaryDisplayItem;
i _secondaryDisplayItemRole;
@"SBPBDisplayItemLayoutAttributes" _secondaryLayoutAttributes;
B _hidden;
{?="centerDisplayItemRole"b1"secondaryDisplayItemRole"b1} _has;
```

## Instance methods

```
-[SBPBAppLayout writeTo:];
-[SBPBAppLayout hash];
-[SBPBAppLayout description];
-[SBPBAppLayout readFrom:];
-[SBPBAppLayout copyWithZone:];
-[SBPBAppLayout isEqual:];
-[SBPBAppLayout dictionaryRepresentation];
-[SBPBAppLayout testSet_centerLayoutAttributes:];
-[SBPBAppLayout testSet_centerDisplayItem:];
-[SBPBAppLayout testSet_primaryDisplayItem:];
-[SBPBAppLayout testSet_primaryLayoutAttributes:];
-[SBPBAppLayout testSet_secondaryDisplayItem:];
-[SBPBAppLayout testSet_secondaryLayoutAttributes:];
-[SBPBAppLayout test_centerDisplayItem];
-[SBPBAppLayout test_centerLayoutAttributes];
-[SBPBAppLayout test_primaryDisplayItem];
-[SBPBAppLayout test_primaryLayoutAttributes];
-[SBPBAppLayout test_secondaryDisplayItem];
-[SBPBAppLayout test_secondaryLayoutAttributes];
```
