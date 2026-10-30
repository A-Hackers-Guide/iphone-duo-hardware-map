# `WFHotspotCell`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewCell`
- Protocols: `WFNetworkCell`
- 12 instance variables, 19 properties, 33 instance methods, 0 class methods

## Instance variables

```
B _personalHotspot;
B _secure;
Q _bars;
@"NSString" _title;
@"WFHotspotDetails" _hotspotDetails;
@"UIStackView" _stackView;
@"UILabel" _nameLabel;
@"WFHotspotDetailsView" _hotspotDetailsView;
@"NSLayoutConstraint" _stackViewTopConstraint;
@"NSLayoutConstraint" _stackViewBottomConstraint;
@"WFAssociationStateView" _associationStateView;
@"NSLayoutConstraint" _stackViewLeadingConstraint;
```

## Properties

```
@property (T@"UIStackView",W,N,V_stackView) stackView;
@property (T@"UILabel",W,N,V_nameLabel) nameLabel;
@property (T@"WFHotspotDetailsView",W,N,V_hotspotDetailsView) hotspotDetailsView;
@property (T@"NSLayoutConstraint",W,N,V_stackViewTopConstraint) stackViewTopConstraint;
@property (T@"NSLayoutConstraint",W,N,V_stackViewBottomConstraint) stackViewBottomConstraint;
@property (T@"WFAssociationStateView",W,N,V_associationStateView) associationStateView;
@property (T@"NSLayoutConstraint",W,N,V_stackViewLeadingConstraint) stackViewLeadingConstraint;
@property (T@"NSString",C,N,V_title) title;
@property (T@"NSString",C,D,N) subtitle;
@property (TB,N,V_secure) secure;
@property (Tq,D,N) state;
@property (TQ,N,V_bars) bars;
@property (TB,N,V_personalHotspot) personalHotspot;
@property (T@"WFHotspotDetails",&,N,V_hotspotDetails) hotspotDetails;
@property (TB,D,N) connectionError;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WFHotspotCell setBars:];
-[WFHotspotCell setSecure:];
-[WFHotspotCell setState:];
-[WFHotspotCell setConnectionError:];
-[WFHotspotCell setSubtitle:];
-[WFHotspotCell bars];
-[WFHotspotCell nameLabel];
-[WFHotspotCell title];
-[WFHotspotCell prepareForReuse];
-[WFHotspotCell stackView];
-[WFHotspotCell setStackView:];
-[WFHotspotCell traitCollectionDidChange:];
-[WFHotspotCell setTitle:];
-[WFHotspotCell state];
-[WFHotspotCell awakeFromNib];
-[WFHotspotCell setNameLabel:];
-[WFHotspotCell secure];
-[WFHotspotCell setStackViewLeadingConstraint:];
-[WFHotspotCell stackViewLeadingConstraint];
-[WFHotspotCell _verticalPadding];
-[WFHotspotCell setStackViewBottomConstraint:];
-[WFHotspotCell setStackViewTopConstraint:];
-[WFHotspotCell stackViewBottomConstraint];
-[WFHotspotCell stackViewTopConstraint];
-[WFHotspotCell setPersonalHotspot:];
-[WFHotspotCell _adjustStackViewPadding];
-[WFHotspotCell personalHotspot];
-[WFHotspotCell associationStateView];
-[WFHotspotCell hotspotDetails];
-[WFHotspotCell hotspotDetailsView];
-[WFHotspotCell setAssociationStateView:];
-[WFHotspotCell setHotspotDetails:];
-[WFHotspotCell setHotspotDetailsView:];
```
