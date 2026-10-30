# `SBProactiveHomeScreenSuggestionProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ATXHomeScreenSuggestionClientObserver`
- 3 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"ATXHomeScreenPrediction" _currentPrediction;
@"SBHIconManager" _iconManager;
```

## Properties

```
@property (T@"SBHIconManager",R,W,N,V_iconManager) iconManager;
@property (T@"ATXHomeScreenPrediction",&,N,V_currentPrediction) currentPrediction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBProactiveHomeScreenSuggestionProvider iconManager];
-[SBProactiveHomeScreenSuggestionProvider setCurrentPrediction:];
-[SBProactiveHomeScreenSuggestionProvider removeObserver:];
-[SBProactiveHomeScreenSuggestionProvider addObserver:];
-[SBProactiveHomeScreenSuggestionProvider currentPrediction];
-[SBProactiveHomeScreenSuggestionProvider rootFolder];
-[SBProactiveHomeScreenSuggestionProvider initWithIconManager:];
-[SBProactiveHomeScreenSuggestionProvider iconModel];
-[SBProactiveHomeScreenSuggestionProvider suggestionClientDidRefreshSuggestions:];
-[SBProactiveHomeScreenSuggestionProvider _iconDataSourceInIcon:withUniqueIdentifier:extensionBundleIdentifier:widgetKind:suggestionSource:];
-[SBProactiveHomeScreenSuggestionProvider _makeDataSourceForAtxWidget:];
-[SBProactiveHomeScreenSuggestionProvider _supportedElementClasses];
-[SBProactiveHomeScreenSuggestionProvider processUpdatedPredictions:];
-[SBProactiveHomeScreenSuggestionProvider updatePredictions];
```
