
  
  

  


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <meta http-equiv="content-type" content="text/html;charset=UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
        <title>expectations/selenium_expectations/jquery.sleep.js at master from xto's SUTA - GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="http://github.com/fluidicon.png" title="GitHub" />

    <link href="http://assets3.github.com/stylesheets/bundle_common.css?63ff269517af5aa36d599ef776c01fea4e9c2d8a" media="screen" rel="stylesheet" type="text/css" />
<link href="http://assets2.github.com/stylesheets/bundle_github.css?63ff269517af5aa36d599ef776c01fea4e9c2d8a" media="screen" rel="stylesheet" type="text/css" />

    <script type="text/javascript" charset="utf-8">
      var GitHub = {}
      var github_user = 'nicholaslemay'
      
    </script>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js" type="text/javascript"></script>
    <script src="http://assets1.github.com/javascripts/bundle_common.js?63ff269517af5aa36d599ef776c01fea4e9c2d8a" type="text/javascript"></script>
<script src="http://assets1.github.com/javascripts/bundle_github.js?63ff269517af5aa36d599ef776c01fea4e9c2d8a" type="text/javascript"></script>

        <script type="text/javascript" charset="utf-8">
      GitHub.spy({
        repo: "xto/SUTA"
      })
    </script>

    
  
    
  

  <link href="http://github.com/xto/SUTA/commits/master.atom" rel="alternate" title="Recent Commits to SUTA:master" type="application/atom+xml" />

        <meta name="description" content="Simplified Unit Testing Add-on for phpunit" />
    <script type="text/javascript">
      GitHub.nameWithOwner = GitHub.nameWithOwner || "xto/SUTA";
      GitHub.currentRef = "master";
    </script>
  

            <script type="text/javascript">
      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-3769691-2']);
      _gaq.push(['_trackPageview']);
      (function() {
        var ga = document.createElement('script');
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        ga.setAttribute('async', 'true');
        document.documentElement.firstChild.appendChild(ga);
      })();
    </script>

  </head>

  

  <body>
    
    

    

    <div class="subnavd" id="main">
      <div id="header" class="pageheaded">
        <div class="site">
          <div class="logo">
            <a href="https://github.com"><img src="/images/modules/header/logov3.png" alt="github" /></a>
          </div>
          
            


  
    <div class="userbox">
      <div class="inner">
        <div class="avatarname">
          <a href="http://github.com/nicholaslemay"><img alt="" height="20" src="http://www.gravatar.com/avatar/99aacb023a455c3f532655c3b23fed7b?s=20&amp;d=http%3A%2F%2Fgithub.com%2Fimages%2Fgravatars%2Fgravatar-20.png" width="20" /></a>
          <a href="http://github.com/nicholaslemay" class="name">nicholaslemay</a>

          
          
        </div>
        <ul class="usernav">
          <li><a href="https://github.com">Dashboard</a></li>
          <li>
            
            <a href="https://github.com/inbox">Inbox</a>
            <a href="https://github.com/inbox" class="unread_count ">0</a>
          </li>
          <li><a href="https://github.com/account">Account Settings</a></li>
                    <li><a href="/logout">Log Out</a></li>
        </ul>
      </div>
    </div><!-- /.userbox -->
  


          
          <div class="topsearch">
  
    <form action="/search" id="top_search_form" method="get">
      <a href="/search" class="advanced-search tooltipped downwards" title="Advanced Search">Advanced Search</a>
      <input type="search" class="search my_repos_autocompleter" name="q" results="5" placeholder="Search&hellip;" /> <input type="submit" value="Search" class="button" />
      <input type="hidden" name="type" value="Everything" />
      <input type="hidden" name="repo" value="" />
      <input type="hidden" name="langOverride" value="" />
      <input type="hidden" name="start_value" value="1" />
    </form>
  
  
    <ul class="nav">
      <li><a href="/explore">Explore GitHub</a></li>
      <li><a href="http://gist.github.com">Gist</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="http://help.github.com">Help</a></li>
    </ul>
  
</div>

        </div>
      </div>

      
      
        
    <div class="site">
      <div class="pagehead repohead vis-public   ">
        <h1>
          <a href="/xto">xto</a> / <strong><a href="http://github.com/xto/SUTA">SUTA</a></strong>
          
          
        </h1>

        
    <ul class="actions">
      
      
        <li class="for-owner" style="display:none"><a href="https://github.com/xto/SUTA/edit" class="minibutton btn-admin "><span><span class="icon"></span>Admin</span></a></li>
        <li>
          <a href="/xto/SUTA/toggle_watch" class="minibutton btn-watch " id="watch_button" style="display:none"><span><span class="icon"></span>Watch</span></a>
          <a href="/xto/SUTA/toggle_watch" class="minibutton btn-watch " id="unwatch_button" style="display:none"><span><span class="icon"></span>Unwatch</span></a>
        </li>
        
          <li class="for-notforked" style="display:none"><a href="/xto/SUTA/fork" class="minibutton btn-fork " id="fork_button" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', '2156add0836ffe0b9ef776987ea4aa606e857238'); f.appendChild(s);f.submit();return false;"><span><span class="icon"></span>Fork</span></a></li>
          <li class="for-hasfork" style="display:none"><a href="#" class="minibutton btn-fork " id="your_fork_button"><span><span class="icon"></span>Your Fork</span></a></li>
          <li id="pull_request_item" style="display:none"><a href="/xto/SUTA/pull_request/" class="minibutton btn-pull-request "><span><span class="icon"></span>Pull Request</span></a></li>
          <li><a href="#" class="minibutton btn-download " id="download_button"><span><span class="icon"></span>Download Source</span></a></li>
        
      
      <li class="repostats">
        <ul class="repo-stats">
          <li class="watchers"><a href="/xto/SUTA/watchers" title="Watchers" class="tooltipped downwards">3</a></li>
          <li class="forks"><a href="/xto/SUTA/network" title="Forks" class="tooltipped downwards">1</a></li>
        </ul>
      </li>
    </ul>


        <ul class="tabs">
  <li><a href="http://github.com/xto/SUTA/tree/master" class="selected" highlight="repo_source">Source</a></li>
  <li><a href="http://github.com/xto/SUTA/commits/master" highlight="repo_commits">Commits</a></li>

  
  <li><a href="/xto/SUTA/network" highlight="repo_network">Network (1)</a></li>

  
    <li><a href="/xto/SUTA/forkqueue" highlight="repo_fork_queue">Fork Queue</a></li>
  

  
    
    <li><a href="/xto/SUTA/issues" highlight="issues">Issues (0)</a></li>
  

  
    
    <li><a href="/xto/SUTA/downloads">Downloads (0)</a></li>
  

  
    
    <li><a href="http://wiki.github.com/xto/SUTA/">Wiki (1)</a></li>
  

  <li><a href="/xto/SUTA/graphs" highlight="repo_graphs">Graphs</a></li>

  <li class="contextswitch nochoices">
    <span class="toggle leftwards" >
      <em>Branch:</em>
      <code>master</code>
    </span>
  </li>
</ul>

<div style="display:none" id="pl-description"><p><em class="placeholder">click here to add a description</em></p></div>
<div style="display:none" id="pl-homepage"><p><em class="placeholder">click here to add a homepage</em></p></div>

<div class="subnav-bar">
  
  <ul>
    <li>
      <a href="#" class="dropdown">Switch Branches (3)</a>
      <ul>
        
          
          
            <li><a href="/xto/SUTA/blob/gh-pages/expectations/selenium_expectations/jquery.sleep.js" action="show">gh-pages</a></li>
          
        
          
            <li><strong>master &#x2713;</strong></li>
            
          
          
            <li><a href="/xto/SUTA/blob/releases/expectations/selenium_expectations/jquery.sleep.js" action="show">releases</a></li>
          
        
      </ul>
    </li>
    <li>
      <a href="#" class="dropdown defunct">Switch Tags (0)</a>
      
    </li>
    <li>
    
    <a href="/xto/SUTA/branches" class="manage">Branch List</a>
    
    </li>
  </ul>
</div>









        
    <div id="repo_details" class="metabox clearfix ">
      <div id="repo_details_loader" class="metabox-loader" style="display:none">Sending Request&hellip;</div>

      

      <div id="repository_description" rel="repository_description_edit">
        
          <p>Simplified Unit Testing Add-on for phpunit
            <span id="read_more" style="display:none">&mdash; <a href="#readme">Read more</a></span>
          </p>
        
      </div>
      <div id="repository_description_edit" style="display:none;" class="inline-edit">
        <form action="/xto/SUTA/edit/update" method="post"><div style="margin:0;padding:0"><input name="authenticity_token" type="hidden" value="2156add0836ffe0b9ef776987ea4aa606e857238" /></div>
          <input type="hidden" name="field" value="repository_description">
          <input type="text" class="textfield" name="value" value="Simplified Unit Testing Add-on for phpunit">
          <div class="form-actions">
            <button class="minibutton"><span>Save</span></button> &nbsp; <a href="#" class="cancel">Cancel</a>
          </div>
        </form>
      </div>

      
      <div class="repository-homepage" id="repository_homepage" rel="repository_homepage_edit">
        <p><a href="http://xto.github.com/SUTA/" rel="nofollow">http://xto.github.com/SUTA/</a></p>
      </div>
      <div id="repository_homepage_edit" style="display:none;" class="inline-edit">
        <form action="/xto/SUTA/edit/update" method="post"><div style="margin:0;padding:0"><input name="authenticity_token" type="hidden" value="2156add0836ffe0b9ef776987ea4aa606e857238" /></div>
          <input type="hidden" name="field" value="repository_homepage">
          <input type="text" class="textfield" name="value" value="http://xto.github.com/SUTA/">
          <div class="form-actions">
            <button class="minibutton"><span>Save</span></button> &nbsp; <a href="#" class="cancel">Cancel</a>
          </div>
        </form>
      </div>

      <div class="rule "></div>

      <div id="url_box" class="url-box">
        <ul class="clone-urls">
          <li id="private_clone_url" style="display:none"><a href="git@github.com:xto/SUTA.git" data-permissions="Read+Write">Private</a></li>
          
            <li id="public_clone_url"><a href="git://github.com/xto/SUTA.git" data-permissions="Read-Only">Read-Only</a></li>
            <li id="http_clone_url"><a href="http://github.com/xto/SUTA.git" data-permissions="Read-Only">HTTP Read-Only</a></li>
          
        </ul>
        <input type="text" spellcheck="false" id="url_field" class="url-field" />
              <span style="display:none" id="url_box_clippy"></span>
      <span id="clippy_tooltip_url_box_clippy" class="clippy-tooltip tooltipped" title="copy to clipboard">
      <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
              width="14"
              height="14"
              class="clippy"
              id="clippy" >
      <param name="movie" value="/flash/clippy.swf?v5"/>
      <param name="allowScriptAccess" value="always" />
      <param name="quality" value="high" />
      <param name="scale" value="noscale" />
      <param NAME="FlashVars" value="id=url_box_clippy&amp;copied=&amp;copyto=">
      <param name="bgcolor" value="#FFFFFF">
      <param name="wmode" value="opaque">
      <embed src="/flash/clippy.swf?v5"
             width="14"
             height="14"
             name="clippy"
             quality="high"
             allowScriptAccess="always"
             type="application/x-shockwave-flash"
             pluginspage="http://www.macromedia.com/go/getflashplayer"
             FlashVars="id=url_box_clippy&amp;copied=&amp;copyto="
             bgcolor="#FFFFFF"
             wmode="opaque"
      />
      </object>
      </span>

        <p id="url_description">This URL has <strong>Read+Write</strong> access</p>
      </div>
    </div>


        

      </div><!-- /.pagehead -->

      









<script type="text/javascript">
  GitHub.currentCommitRef = "master"
  GitHub.currentRepoOwner = "xto"
  GitHub.currentRepo = "SUTA"
  GitHub.downloadRepo = '/xto/SUTA/archives/master'
  
    GitHub.hasWriteAccess = true
    GitHub.watchingRepo = true
    GitHub.ignoredRepo = false
    GitHub.hasForkOfRepo = ""
    GitHub.hasForked = false
  

  
</script>










  <div id="commit">
    <div class="group">
        
  <div class="envelope commit">
    <div class="human">
      
        <div class="message"><pre><a href="/xto/SUTA/commit/3deb27ac5b8ab6b56f8755350d2ddd50157cb60c">updating package.xml to reflect upcomiong package</a> </pre></div>
      

      <div class="actor">
        <div class="gravatar">
          
          <img alt="" height="30" src="http://www.gravatar.com/avatar/99aacb023a455c3f532655c3b23fed7b?s=30&amp;d=http%3A%2F%2Fgithub.com%2Fimages%2Fgravatars%2Fgravatar-30.png" width="30" />
        </div>
        <div class="name"><a href="/nicholaslemay">nicholaslemay</a> <span>(author)</span></div>
        <div class="date">
          <abbr class="relatize" title="2010-03-16 07:35:31">Tue Mar 16 07:35:31 -0700 2010</abbr>
        </div>
      </div>

      

    </div>
    <div class="machine">
      <span>c</span>ommit&nbsp;&nbsp;<a href="/xto/SUTA/commit/3deb27ac5b8ab6b56f8755350d2ddd50157cb60c" hotkey="c">3deb27ac5b8ab6b56f8755350d2ddd50157cb60c</a><br />
      <span>t</span>ree&nbsp;&nbsp;&nbsp;&nbsp;<a href="/xto/SUTA/tree/3deb27ac5b8ab6b56f8755350d2ddd50157cb60c" hotkey="t">06c5e7c11cd16cda1bd2df7a08ffebedd1b3a93a</a><br />
      
        <span>p</span>arent&nbsp;
        
        <a href="/xto/SUTA/tree/adf7e9fd680f8b873ea3342e9e71266322a889f5" hotkey="p">adf7e9fd680f8b873ea3342e9e71266322a889f5</a>
      

    </div>
  </div>

    </div>
  </div>



  
    <div id="path">
      <b><a href="/xto/SUTA/tree/master">SUTA</a></b> / <a href="/xto/SUTA/tree/master/expectations">expectations</a> / <a href="/xto/SUTA/tree/master/expectations/selenium_expectations">selenium_expectations</a> / jquery.sleep.js       <span style="display:none" id="clippy_700">expectations/selenium_expectations/jquery.sleep.js</span>
      
      <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
              width="110"
              height="14"
              class="clippy"
              id="clippy" >
      <param name="movie" value="/flash/clippy.swf?v5"/>
      <param name="allowScriptAccess" value="always" />
      <param name="quality" value="high" />
      <param name="scale" value="noscale" />
      <param NAME="FlashVars" value="id=clippy_700&amp;copied=copied!&amp;copyto=copy to clipboard">
      <param name="bgcolor" value="#FFFFFF">
      <param name="wmode" value="opaque">
      <embed src="/flash/clippy.swf?v5"
             width="110"
             height="14"
             name="clippy"
             quality="high"
             allowScriptAccess="always"
             type="application/x-shockwave-flash"
             pluginspage="http://www.macromedia.com/go/getflashplayer"
             FlashVars="id=clippy_700&amp;copied=copied!&amp;copyto=copy to clipboard"
             bgcolor="#FFFFFF"
             wmode="opaque"
      />
      </object>
      

    </div>

    <div id="files">
      <div class="file">
        <div class="meta">
          <div class="info">
            <span>100644</span>
            <span>31 lines (30 sloc)</span>
            <span>0.775 kb</span>
          </div>
          <div class="actions">
            
              <a style="display:none;" id="file-edit-link" href="#" rel="/xto/SUTA/file-edit/__ref__/expectations/selenium_expectations/jquery.sleep.js">edit</a>
            
            <a href="/xto/SUTA/raw/master/expectations/selenium_expectations/jquery.sleep.js" id="raw-url">raw</a>
            
              <a href="/xto/SUTA/blame/master/expectations/selenium_expectations/jquery.sleep.js">blame</a>
            
            <a href="/xto/SUTA/commits/master/expectations/selenium_expectations/jquery.sleep.js">history</a>
          </div>
        </div>
        
  <div class="data syntax type-js">
    
      <table cellpadding="0" cellspacing="0">
        <tr>
          <td>
            
            <pre class="line_numbers">
<span id="LID1" rel="#L1">1</span>
<span id="LID2" rel="#L2">2</span>
<span id="LID3" rel="#L3">3</span>
<span id="LID4" rel="#L4">4</span>
<span id="LID5" rel="#L5">5</span>
<span id="LID6" rel="#L6">6</span>
<span id="LID7" rel="#L7">7</span>
<span id="LID8" rel="#L8">8</span>
<span id="LID9" rel="#L9">9</span>
<span id="LID10" rel="#L10">10</span>
<span id="LID11" rel="#L11">11</span>
<span id="LID12" rel="#L12">12</span>
<span id="LID13" rel="#L13">13</span>
<span id="LID14" rel="#L14">14</span>
<span id="LID15" rel="#L15">15</span>
<span id="LID16" rel="#L16">16</span>
<span id="LID17" rel="#L17">17</span>
<span id="LID18" rel="#L18">18</span>
<span id="LID19" rel="#L19">19</span>
<span id="LID20" rel="#L20">20</span>
<span id="LID21" rel="#L21">21</span>
<span id="LID22" rel="#L22">22</span>
<span id="LID23" rel="#L23">23</span>
<span id="LID24" rel="#L24">24</span>
<span id="LID25" rel="#L25">25</span>
<span id="LID26" rel="#L26">26</span>
<span id="LID27" rel="#L27">27</span>
<span id="LID28" rel="#L28">28</span>
<span id="LID29" rel="#L29">29</span>
<span id="LID30" rel="#L30">30</span>
<span id="LID31" rel="#L31">31</span>
</pre>
          </td>
          <td width="100%">
            
              <div class="highlight"><pre><div class="line" id="LC1"><span class="cm">/*</span></div><div class="line" id="LC2"><span class="cm">	Sleep by Mark Hughes</span></div><div class="line" id="LC3"><span class="cm">	http://www.360Gamer.net/</span></div><div class="line" id="LC4">&nbsp;</div><div class="line" id="LC5"><span class="cm">	Usage:</span></div><div class="line" id="LC6"><span class="cm">		jQuery.sleep ( 3, function()</span></div><div class="line" id="LC7"><span class="cm">		{</span></div><div class="line" id="LC8"><span class="cm">			alert ( &quot;I slept for 3 seconds!&quot; );</span></div><div class="line" id="LC9"><span class="cm">		});</span></div><div class="line" id="LC10"><span class="cm">	Use at free will, distribute free of charge</span></div><div class="line" id="LC11"><span class="cm">*/</span></div><div class="line" id="LC12"><span class="p">;(</span><span class="kd">function</span><span class="p">(</span><span class="nx">jQuery</span><span class="p">)</span></div><div class="line" id="LC13"><span class="p">{</span></div><div class="line" id="LC14">	<span class="kd">var</span> <span class="nx">_sleeptimer</span><span class="p">;</span></div><div class="line" id="LC15">	<span class="nx">jQuery</span><span class="p">.</span><span class="nx">sleep</span> <span class="o">=</span> <span class="kd">function</span><span class="p">(</span> <span class="nx">time2sleep</span><span class="p">,</span> <span class="nx">callback</span> <span class="p">)</span></div><div class="line" id="LC16">	<span class="p">{</span></div><div class="line" id="LC17">		<span class="nx">jQuery</span><span class="p">.</span><span class="nx">sleep</span><span class="p">.</span><span class="nx">_sleeptimer</span> <span class="o">=</span> <span class="nx">time2sleep</span><span class="p">;</span></div><div class="line" id="LC18">		<span class="nx">jQuery</span><span class="p">.</span><span class="nx">sleep</span><span class="p">.</span><span class="nx">_cback</span> <span class="o">=</span> <span class="nx">callback</span><span class="p">;</span></div><div class="line" id="LC19">		<span class="nx">jQuery</span><span class="p">.</span><span class="nx">sleep</span><span class="p">.</span><span class="nx">timer</span> <span class="o">=</span> <span class="nx">setInterval</span><span class="p">(</span><span class="s1">&#39;jQuery.sleep.count()&#39;</span><span class="p">,</span> <span class="mi">1000</span><span class="p">);</span></div><div class="line" id="LC20">	<span class="p">}</span></div><div class="line" id="LC21">	<span class="nx">jQuery</span><span class="p">.</span><span class="nx">extend</span> <span class="p">(</span><span class="nx">jQuery</span><span class="p">.</span><span class="nx">sleep</span><span class="p">,</span> <span class="p">{</span></div><div class="line" id="LC22">		<span class="nx">current_i</span> <span class="o">:</span> <span class="mi">1</span><span class="p">,</span></div><div class="line" id="LC23">		<span class="nx">_sleeptimer</span> <span class="o">:</span> <span class="mi">0</span><span class="p">,</span></div><div class="line" id="LC24">		<span class="nx">_cback</span> <span class="o">:</span> <span class="kc">null</span><span class="p">,</span></div><div class="line" id="LC25">		<span class="nx">timer</span> <span class="o">:</span> <span class="kc">null</span><span class="p">,</span></div><div class="line" id="LC26">		<span class="nx">count</span> <span class="o">:</span> <span class="kd">function</span><span class="p">()</span></div><div class="line" id="LC27">		<span class="p">{</span></div><div class="line" id="LC28">			<span class="k">if</span> <span class="p">(</span> <span class="nx">jQuery</span><span class="p">.</span><span class="nx">sleep</span><span class="p">.</span><span class="nx">current_i</span> <span class="o">===</span> <span class="nx">jQuery</span><span class="p">.</span><span class="nx">sleep</span><span class="p">.</span><span class="nx">_sleeptimer</span> <span class="p">)</span></div><div class="line" id="LC29">			<span class="p">{</span></div><div class="line" id="LC30">				<span class="nx">clearInterval</span><span class="p">(</span><span class="nx">jQuery</span><span class="p">.</span><span class="nx">sleep</span><span class="p">.</span><span class="nx">timer</span><span class="p">);</span></div><div class="line" id="LC31">				<span class="nx">jQuery</span><span class="p">.</span><span class="nx">sleep</span><span class="p">.</span><span class="nx">_cback</span><span class="p">.</span><span class="nx">call</span><span class="p">(</span><span class="k">this</span><span class="p">);</span></div></pre></div>
            
          </td>
        </tr>
      </table>
    
  </div>


      </div>
    </div>

  


    </div>
  
      

      <div class="push"></div>
    </div>

    <div id="footer">
      <div class="site">
        <div class="info">
          <div class="links">
            <a href="http://github.com/blog"><b>Blog</b></a> |
            <a href="http://support.github.com/">Support</a> |
            <a href="http://github.com/training">Training</a> |
            <a href="http://github.com/contact">Contact</a> |
            <a href="http://develop.github.com">API</a> |
            <a href="http://status.github.com">Status</a> |
            <a href="http://twitter.com/github">Twitter</a> |
            <a href="http://help.github.com">Help</a> |
            <a href="http://github.com/security">Security</a>
          </div>
          <div class="company">
            &copy;
            2010
            <span id="_rrt" title="0.33497s from fe2.rs.github.com">GitHub</span> Inc.
            All rights reserved. |
            <a href="/site/terms">Terms of Service</a> |
            <a href="/site/privacy">Privacy Policy</a>
          </div>
        </div>
        <div class="sponsor">
          <div>
            Powered by the <a href="http://www.rackspace.com ">Dedicated
            Servers</a> and<br/> <a href="http://www.rackspacecloud.com">Cloud
            Computing</a> of Rackspace Hosting<span>&reg;</span>
          </div>
          <a href="http://www.rackspace.com">
            <img alt="Dedicated Server" src="http://assets1.github.com/images/modules/footer/rackspace_logo.png?63ff269517af5aa36d599ef776c01fea4e9c2d8a" />
          </a>
        </div>
      </div>
    </div>

    <script>window._auth_token = "2156add0836ffe0b9ef776987ea4aa606e857238"</script>
    
    
  </body>
</html>

