# `WTWritingToolsDelegate_Proposed_v3` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 1 properties, 10 instance methods, 0 class methods

## Properties

```
@property (TB,?,R,N) includesTextListMarkers;
```

## Instance methods

```
-[WTWritingToolsDelegate_Proposed_v3 didBeginWritingToolsSession:contexts:];
-[WTWritingToolsDelegate_Proposed_v3 compositionSession:didReceiveText:replacementRange:inContext:finished:];
-[WTWritingToolsDelegate_Proposed_v3 willBeginWritingToolsSession:requestContexts:];
-[WTWritingToolsDelegate_Proposed_v3 didEndWritingToolsSession:accepted:];
-[WTWritingToolsDelegate_Proposed_v3 proofreadingSession:didUpdateState:forSuggestionWithUUID:inContext:];
-[WTWritingToolsDelegate_Proposed_v3 proofreadingSession:didReceiveSuggestions:processedRange:inContext:finished:];
-[WTWritingToolsDelegate_Proposed_v3 writingToolsSession:didReceiveAction:];
-[WTWritingToolsDelegate_Proposed_v3 includesTextListMarkers];
-[WTWritingToolsDelegate_Proposed_v3 requestContextsForScope:completion:];
-[WTWritingToolsDelegate_Proposed_v3 supportsWritingToolsAction:];
```
