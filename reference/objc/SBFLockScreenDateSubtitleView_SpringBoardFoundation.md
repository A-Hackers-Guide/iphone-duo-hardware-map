# `SBFLockScreenDateSubtitleView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 4 instance variables, 7 properties, 22 instance methods, 3 class methods

## Instance variables

```
@"SBUILegibilityLabel" _label;
@"UIView" _accessoryView;
@"_UILegibilitySettings" _legibilitySettings;
d _strength;
```

## Properties

```
@property (T@"_UILegibilitySettings",&,N,V_legibilitySettings) legibilitySettings;
@property (Td,N,V_strength) strength;
@property (T@"UIFont",&,N) font;
@property (Td,R,N) baselineOffsetFromOrigin;
@property (Td,R,N) baselineOffsetFromBottom;
@property (T@"NSString",&,N) string;
@property (T@"UIView",&,N,V_accessoryView) accessoryView;
```

## Class methods

```
+[SBFLockScreenDateSubtitleView labelFont];
+[SBFLockScreenDateSubtitleView labelFontMetrics];
+[SBFLockScreenDateSubtitleView scaledFontSize:withMaximumFontSizeCategory:];
```

## Instance methods

```
-[SBFLockScreenDateSubtitleView accessoryView];
-[SBFLockScreenDateSubtitleView strength];
-[SBFLockScreenDateSubtitleView init];
-[SBFLockScreenDateSubtitleView setStrength:];
-[SBFLockScreenDateSubtitleView dealloc];
-[SBFLockScreenDateSubtitleView setAccessoryView:];
-[SBFLockScreenDateSubtitleView _updateForCurrentSizeCategory];
-[SBFLockScreenDateSubtitleView accessoryViewFrame];
-[SBFLockScreenDateSubtitleView interItemSpacing];
-[SBFLockScreenDateSubtitleView string];
-[SBFLockScreenDateSubtitleView layoutSubviews];
-[SBFLockScreenDateSubtitleView setString:];
-[SBFLockScreenDateSubtitleView sizeThatFits:];
-[SBFLockScreenDateSubtitleView legibilitySettings];
-[SBFLockScreenDateSubtitleView font];
-[SBFLockScreenDateSubtitleView setLegibilitySettings:];
-[SBFLockScreenDateSubtitleView baselineOffsetFromBottom];
-[SBFLockScreenDateSubtitleView setFont:];
-[SBFLockScreenDateSubtitleView baselineOffsetFromOrigin];
-[SBFLockScreenDateSubtitleView initWithString:accessoryView:];
-[SBFLockScreenDateSubtitleView subtitleLabelCharacterOverflowInsets];
-[SBFLockScreenDateSubtitleView subtitleLabelFrame];
```
