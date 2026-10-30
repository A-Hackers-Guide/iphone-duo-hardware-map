# `SBFLockScreenDateSubtitleDateView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFLockScreenDateSubtitleView`
- 4 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSTimeZone" _timeZone;
B _useCompactDateFormat;
@"NSDate" _date;
d _alignmentPercent;
```

## Properties

```
@property (Td,N,V_alignmentPercent) alignmentPercent;
@property (T@"NSDate",&,N,V_date) date;
@property (TB,N,V_useCompactDateFormat) useCompactDateFormat;
```

## Class methods

```
+[SBFLockScreenDateSubtitleDateView scaledFontSize:withMaximumFontSizeCategory:];
```

## Instance methods

```
-[SBFLockScreenDateSubtitleDateView _setDate:inTimeZone:];
-[SBFLockScreenDateSubtitleDateView initWithDate:];
-[SBFLockScreenDateSubtitleDateView useCompactDateFormat];
-[SBFLockScreenDateSubtitleDateView setDate:];
-[SBFLockScreenDateSubtitleDateView setUseCompactDateFormat:];
-[SBFLockScreenDateSubtitleDateView dealloc];
-[SBFLockScreenDateSubtitleDateView date];
-[SBFLockScreenDateSubtitleDateView setAlignmentPercent:];
-[SBFLockScreenDateSubtitleDateView setLegibilitySettings:];
-[SBFLockScreenDateSubtitleDateView alignmentPercent];
-[SBFLockScreenDateSubtitleDateView _updateDateLabelForCompact];
```
