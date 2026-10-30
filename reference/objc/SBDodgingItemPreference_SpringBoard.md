# `SBDodgingItemPreference`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _updateInteractively;
B _canBePositionedOutsideContainerBounds;
Q _dodgingAxisMask;
@"NSSet" _excludedDodgingIdentifiers;
{CGSize="width"d"height"d} _preferredSize;
{CGPoint="x"d"y"d} _preferredCenter;
{CGSize="width"d"height"d} _minimumSize;
```

## Properties

```
@property (T{CGSize=dd},R,N,V_preferredSize) preferredSize;
@property (T{CGPoint=dd},R,N,V_preferredCenter) preferredCenter;
@property (TB,R,N,GisUpdatingInteractively,V_updateInteractively) updateInteractively;
@property (TQ,R,N,V_dodgingAxisMask) dodgingAxisMask;
@property (T{CGSize=dd},R,N,V_minimumSize) minimumSize;
@property (TB,R,N,V_canBePositionedOutsideContainerBounds) canBePositionedOutsideContainerBounds;
@property (T@"NSSet",R,N,V_excludedDodgingIdentifiers) excludedDodgingIdentifiers;
```

## Instance methods

```
-[SBDodgingItemPreference minimumSize];
-[SBDodgingItemPreference preferredSize];
-[SBDodgingItemPreference dodgingAxisMask];
-[SBDodgingItemPreference preferredCenter];
-[SBDodgingItemPreference canBePositionedOutsideContainerBounds];
-[SBDodgingItemPreference excludedDodgingIdentifiers];
-[SBDodgingItemPreference initWithPreferredSize:preferredCenter:updateInteractively:dodgingAxisMask:minimumSize:canBePositionedOutsideContainerBounds:excludedDodgingIdentifiers:];
-[SBDodgingItemPreference isUpdatingInteractively];
```
