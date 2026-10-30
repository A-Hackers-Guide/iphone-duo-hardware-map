# `_UINavigationBarTitleRenamerRemoteSession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UINavigationBarTitleRenamerSession`
- Protocols: `_UIOverlayServiceDelegate`, `_UIOServiceConnectionObserver`, `BSXPCSecureCoding`
- 5 instance variables, 9 properties, 42 instance methods, 1 class methods

## Instance variables

```
Q _currentState;
@"FPSandboxingURLWrapper" _urlWrapper;
@"FBSSceneIdentityToken" _sceneOriginIdentityToken;
@"_UIOverlayService" _overlayService;
@"_UIOServiceConnection" _connection;
```

## Properties

```
@property (T@"FPSandboxingURLWrapper",R,N,V_urlWrapper) urlWrapper;
@property (T@"FBSSceneIdentityToken",R,N,V_sceneOriginIdentityToken) sceneOriginIdentityToken;
@property (T@"_UIOverlayService",R,N,V_overlayService) overlayService;
@property (T@"_UIOServiceConnection",&,N,V_connection) connection;
@property (T@"NSURL",R,N) fileURL;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UINavigationBarTitleRenamerRemoteSession supportsBSXPCSecureCoding];
```

## Instance methods

```
-[_UINavigationBarTitleRenamerRemoteSession sessionDidEnd];
-[_UINavigationBarTitleRenamerRemoteSession fileURL];
-[_UINavigationBarTitleRenamerRemoteSession urlWrapper];
-[_UINavigationBarTitleRenamerRemoteSession dealloc];
-[_UINavigationBarTitleRenamerRemoteSession connection];
-[_UINavigationBarTitleRenamerRemoteSession setConnection:];
-[_UINavigationBarTitleRenamerRemoteSession encodeWithBSXPCCoder:];
-[_UINavigationBarTitleRenamerRemoteSession initWithBSXPCCoder:];
-[_UINavigationBarTitleRenamerRemoteSession _client_cancelSessionAndNotify:];
-[_UINavigationBarTitleRenamerRemoteSession _server_cancelSessionAndNotify:];
-[_UINavigationBarTitleRenamerRemoteSession fileRenameDidFail:proposedName:];
-[_UINavigationBarTitleRenamerRemoteSession serviceConnectionDidInvalidate:];
-[_UINavigationBarTitleRenamerRemoteSession _attemptLocalRenameForFileURL:proposedName:completionHandler:];
-[_UINavigationBarTitleRenamerRemoteSession _client_fileRenameDidEnd:];
-[_UINavigationBarTitleRenamerRemoteSession _client_fileRenameDidFail:proposedName:];
-[_UINavigationBarTitleRenamerRemoteSession _client_sessionDidEnd];
-[_UINavigationBarTitleRenamerRemoteSession _client_sessionDidStartInRenamer:];
-[_UINavigationBarTitleRenamerRemoteSession _client_textFieldDidEndEditingWithText:];
-[_UINavigationBarTitleRenamerRemoteSession _client_textFieldShouldEndEditingWithText:];
-[_UINavigationBarTitleRenamerRemoteSession _client_willBeginRenamingWithText:selectedRange:];
-[_UINavigationBarTitleRenamerRemoteSession _isServerSide];
-[_UINavigationBarTitleRenamerRemoteSession _server_fileRenameDidEnd:];
-[_UINavigationBarTitleRenamerRemoteSession _server_fileRenameDidFail:proposedName:];
-[_UINavigationBarTitleRenamerRemoteSession _server_sessionDidEnd];
-[_UINavigationBarTitleRenamerRemoteSession _server_sessionDidStartInRenamer:];
-[_UINavigationBarTitleRenamerRemoteSession _server_textFieldDidEndEditingWithText:];
-[_UINavigationBarTitleRenamerRemoteSession _server_textFieldShouldEndEditingWithText:];
-[_UINavigationBarTitleRenamerRemoteSession _server_willBeginRenamingWithText:selectedRange:];
-[_UINavigationBarTitleRenamerRemoteSession _textFieldDidEndEditingWithText:];
-[_UINavigationBarTitleRenamerRemoteSession _textFieldShouldEndEditingWithText:];
-[_UINavigationBarTitleRenamerRemoteSession _updateSessionWithAction:];
-[_UINavigationBarTitleRenamerRemoteSession _willBeginRenamingWithText:selectedRange:];
-[_UINavigationBarTitleRenamerRemoteSession cancelSession];
-[_UINavigationBarTitleRenamerRemoteSession cancelSessionAndNotify:];
-[_UINavigationBarTitleRenamerRemoteSession createRenamerContentView];
-[_UINavigationBarTitleRenamerRemoteSession fileRenameDidEnd:];
-[_UINavigationBarTitleRenamerRemoteSession initWithFileURL:iconMetadata:error:scene:];
-[_UINavigationBarTitleRenamerRemoteSession initWithSuggestedTitle:iconMetadata:scene:];
-[_UINavigationBarTitleRenamerRemoteSession overlayService];
-[_UINavigationBarTitleRenamerRemoteSession overlayServiceDidInvalidate:];
-[_UINavigationBarTitleRenamerRemoteSession sceneOriginIdentityToken];
-[_UINavigationBarTitleRenamerRemoteSession sessionDidStartInRenamer:];
```
