# `SBWidgetOnboardingLayoutBuilder`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _pinnedWidgets;
@"NSArray" _suggestionWidgets;
```

## Properties

```
@property (T@"NSArray",R,N,V_pinnedWidgets) pinnedWidgets;
@property (T@"NSArray",R,N,V_suggestionWidgets) suggestionWidgets;
```

## Instance methods

```
-[SBWidgetOnboardingLayoutBuilder pinnedWidgets];
-[SBWidgetOnboardingLayoutBuilder defaultMediumCalendarWidgetIcon];
-[SBWidgetOnboardingLayoutBuilder deduplicateInsidePinnedWidgets];
-[SBWidgetOnboardingLayoutBuilder defaultCalendarWidgetIcon:];
-[SBWidgetOnboardingLayoutBuilder defaultFirstSuggestionWidgetIcon:];
-[SBWidgetOnboardingLayoutBuilder defaultLargeFirstSuggestionWidgetIcon];
-[SBWidgetOnboardingLayoutBuilder defaultLargeSecondSuggestionWidgetIcon];
-[SBWidgetOnboardingLayoutBuilder defaultMediumFirstSuggestionWidgetIcon];
-[SBWidgetOnboardingLayoutBuilder defaultMediumSecondSuggestionWidgetIcon];
-[SBWidgetOnboardingLayoutBuilder defaultSecondSuggestionWidgetIcon:];
-[SBWidgetOnboardingLayoutBuilder defaultSmallCalendarWidgetIcon];
-[SBWidgetOnboardingLayoutBuilder defaultSmallClockWidgetIcon];
-[SBWidgetOnboardingLayoutBuilder defaultSmallNotesWidgetIcon];
-[SBWidgetOnboardingLayoutBuilder initWithPinnedWidgets:suggestionWidgets:];
-[SBWidgetOnboardingLayoutBuilder isCalendarWidget:];
-[SBWidgetOnboardingLayoutBuilder isCalendarWidgetIcon:];
-[SBWidgetOnboardingLayoutBuilder isClockWidget:];
-[SBWidgetOnboardingLayoutBuilder isFirstSuggestionActiveWidgetIcon:];
-[SBWidgetOnboardingLayoutBuilder isSecondSuggestionActiveWidgetIcon:];
-[SBWidgetOnboardingLayoutBuilder migratedDefaultWidgets:];
-[SBWidgetOnboardingLayoutBuilder migratedFourWidgets:];
-[SBWidgetOnboardingLayoutBuilder migratedOneLargeWidget:];
-[SBWidgetOnboardingLayoutBuilder migratedOneMediumWidget:];
-[SBWidgetOnboardingLayoutBuilder migratedOneSmallWidget:];
-[SBWidgetOnboardingLayoutBuilder migratedSmallAndMediumWidget:];
-[SBWidgetOnboardingLayoutBuilder migratedThreeWidgets:];
-[SBWidgetOnboardingLayoutBuilder migratedTwoMediumWidgets:];
-[SBWidgetOnboardingLayoutBuilder migratedTwoSmallWidgets:];
-[SBWidgetOnboardingLayoutBuilder suggestionWidgets];
```
