import os


def log(msg):

    os.system('echo ' + msg)


def writeFile(path, content):

    os.makedirs('/'.join(path.split('/')[:-1]))

    with open(path, 'w') as fil: fil.write(content)



class AndroidApp:

    main = 'MainActivity' # main java-file-name


    def __init__(self, name='appy', prefix='com.example.'):

        self.id = prefix + name

        self.name = name

        if os.path.exists(name):

            log('Initialized AndroidApp for existing directory "' + name + '".')

            return

        self.create() 


    def create(self):

        self.addManifest()

        self.addJava()
        
        self.addLayout()


    def addLayout(self):

        path = self.name + '/res/layout/activity_main.xml'

        content = '''<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
  xmlns:tools="http://schemas.android.com/tools" android:layout_width="match_parent"
  android:layout_height="match_parent"
  tools:context=".{app_main}">

  <WebView
    android:layout_width="fill_parent"
    android:layout_height="fill_parent"
    android:id="@+id/webView"
    android:layout_alignParentLeft="true"
    android:layout_alignParentTop="true"
    android:layout_alignParentRight="true"
  />

</RelativeLayout>'''.format(app_main=self.main)

        writeFile(path, content)



    def addJava(self):

        path = self.name + '/java/' + '/'.join(self.id.split('.')) + '/' + self.main + '.java'

        content = 'package ' + self.id + ''';

import android.app.Activity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;


public class MainActivity extends Activity {

  private WebView mywebview;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    mywebview = (WebView)findViewById(R.id.webView);
    WebSettings webSettings = mywebview.getSettings();
    webSettings.setJavaScriptEnabled(true);
    webSettings.setUseWideViewPort(true);
    webSettings.setLoadWithOverviewMode(true);
    mywebview.loadUrl("https://dashing-four-crest.glitch.me");
    mywebview.setWebViewClient(new WebViewClient());
  }


  @Override
  public void onBackPressed(){
    if(mywebview.canGoBack()) {
      mywebview.goBack();
    }
    else {
      super.onBackPressed();
    }
  }
}'''

        writeFile(path, content)


    def addManifest(self):

        path = self.name + '/AndroidManifest.xml'

        content = '''<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="{app_id}" android:installLocation="auto">
  <uses-permission android:name="android.permission.INTERNET"/>
  <application android:label="{app_name}" android:theme="@android:style/Theme.Holo.NoActionBar.Fullscreen">
    <activity android:name=".{app_main}">
      <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
    </activity>
  </application>
</manifest>'''.format(app_id=self.id, app_name=self.name, app_main=self.main)

        writeFile(path, content)



if __name__ == '__main__':
    app_name = 'appy'
    import sys
    if len(sys.argv) > 1:
        app_name = sys.argv[1]
    app = AndroidApp(app_name)
