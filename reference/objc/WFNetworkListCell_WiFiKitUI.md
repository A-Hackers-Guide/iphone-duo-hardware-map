# `WFNetworkListCell`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewCell`
- Protocols: `WFNetworkCell`
- 15 instance variables, 21 properties, 42 instance methods, 0 class methods

## Instance variables

```
B _secure;
B _personalHotspot;
B _connectionError;
Q _bars;
@"NSString" _title;
@"NSString" _subtitle;
@"UIImageView" _signalImageView;
@"UIImageView" _lockImageView;
@"UILabel" _nameLabel;
@"UILabel" _subtitleLabel;
@"UIStackView" _stackView;
@"NSLayoutConstraint" _stackViewTopConstraint;
@"NSLayoutConstraint" _stackViewBottomConstraint;
@"WFAssociationStateView" _associationStateView;
@"NSLayoutConstraint" _signalImageViewCenterConstraint;
```

## Properties

```
@property (T@"UIImageView",W,N,V_signalImageView) signalImageView;
@property (T@"UIImageView",W,N,V_lockImageView) lockImageView;
@property (T@"UILabel",W,N,V_nameLabel) nameLabel;
@property (T@"UILabel",W,N,V_subtitleLabel) subtitleLabel;
@property (T@"UIStackView",W,N,V_stackView) stackView;
@property (T@"NSLayoutConstraint",W,N,V_stackViewTopConstraint) stackViewTopConstraint;
@property (T@"NSLayoutConstraint",W,N,V_stackViewBottomConstraint) stackViewBottomConstraint;
@property (T@"WFAssociationStateView",W,N,V_associationStateView) associationStateView;
@property (T@"NSLayoutConstraint",W,N,V_signalImageViewCenterConstraint) signalImageViewCenterConstraint;
@property (T@"NSString",C,N,V_title) title;
@property (T@"NSString",C,N,V_subtitle) subtitle;
@property (TB,N,V_secure) secure;
@property (Tq,D,N) state;
@property (TQ,N,V_bars) bars;
@property (TB,N,V_personalHotspot) personalHotspot;
@property (T@"WFHotspotDetails",&,D,N) hotspotDetails;
@property (TB,N,V_connectionError) connectionError;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WFNetworkListCell setBars:];
-[WFNetworkListCell setSecure:];
-[WFNetworkListCell subtitleLabel];
-[WFNetworkListCell setState:];
-[WFNetworkListCell setConnectionError:];
-[WFNetworkListCell subtitle];
-[WFNetworkListCell setSubtitleLabel:];
-[WFNetworkListCell setSubtitle:];
-[WFNetworkListCell connectionError];
-[WFNetworkListCell bars];
-[WFNetworkListCell nameLabel];
-[WFNetworkListCell title];
-[WFNetworkListCell prepareForReuse];
-[WFNetworkListCell stackView];
-[WFNetworkListCell setStackView:];
-[WFNetworkListCell traitCollectionDidChange:];
-[WFNetworkListCell setTitle:];
-[WFNetworkListCell awakeFromNib];
-[WFNetworkListCell setNameLabel:];
-[WFNetworkListCell secure];
-[WFNetworkListCell _verticalPadding];
-[WFNetworkListCell setStackViewBottomConstraint:];
-[WFNetworkListCell setStackViewTopConstraint:];
-[WFNetworkListCell stackViewBottomConstraint];
-[WFNetworkListCell stackViewTopConstraint];
-[WFNetworkListCell lockImageView];
-[WFNetworkListCell setLockImageView:];
-[WFNetworkListCell setPersonalHotspot:];
-[WFNetworkListCell _adjustStackViewPadding];
-[WFNetworkListCell signalImageView];
-[WFNetworkListCell personalHotspot];
-[WFNetworkListCell signalImageViewCenterConstraint];
-[WFNetworkListCell _paddingDefaultByDevice];
-[WFNetworkListCell _updateSignalImage];
-[WFNetworkListCell _updateTextColorForLabel:];
-[WFNetworkListCell _updateTintColorForImageView:];
-[WFNetworkListCell associationStateView];
-[WFNetworkListCell imageFromSignalBars:];
-[WFNetworkListCell setAssociationStateView:];
-[WFNetworkListCell setHotspotDetails:];
-[WFNetworkListCell setSignalImageView:];
-[WFNetworkListCell setSignalImageViewCenterConstraint:];
```
