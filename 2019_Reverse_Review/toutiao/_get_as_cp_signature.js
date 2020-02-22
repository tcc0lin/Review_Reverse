var _get_as_cp = function(e) {
  "use strict";
  function r(e, t) {
      var i = (65535 & e) + (65535 & t)
        , n = (e >> 16) + (t >> 16) + (i >> 16);
      return n << 16 | 65535 & i
  }
  function a(e, t) {
      return e << t | e >>> 32 - t
  }
  function s(e, t, i, n, o, s) {
      return r(a(r(r(t, e), r(n, s)), o), i)
  }
  function l(e, t, i, n, o, r, a) {
      return s(t & i | ~t & n, e, t, o, r, a)
  }
  function c(e, t, i, n, o, r, a) {
      return s(t & n | i & ~n, e, t, o, r, a)
  }
  function d(e, t, i, n, o, r, a) {
      return s(t ^ i ^ n, e, t, o, r, a)
  }
  function f(e, t, i, n, o, r, a) {
      return s(i ^ (t | ~n), e, t, o, r, a)
  }
  function u(e, t) {
      e[t >> 5] |= 128 << t % 32,
      e[(t + 64 >>> 9 << 4) + 14] = t;
      var i, n, o, a, s, u = 1732584193, h = -271733879, p = -1732584194, g = 271733878;
      for (i = 0; i < e.length; i += 16)
          n = u,
          o = h,
          a = p,
          s = g,
          u = l(u, h, p, g, e[i], 7, -680876936),
          g = l(g, u, h, p, e[i + 1], 12, -389564586),
          p = l(p, g, u, h, e[i + 2], 17, 606105819),
          h = l(h, p, g, u, e[i + 3], 22, -1044525330),
          u = l(u, h, p, g, e[i + 4], 7, -176418897),
          g = l(g, u, h, p, e[i + 5], 12, 1200080426),
          p = l(p, g, u, h, e[i + 6], 17, -1473231341),
          h = l(h, p, g, u, e[i + 7], 22, -45705983),
          u = l(u, h, p, g, e[i + 8], 7, 1770035416),
          g = l(g, u, h, p, e[i + 9], 12, -1958414417),
          p = l(p, g, u, h, e[i + 10], 17, -42063),
          h = l(h, p, g, u, e[i + 11], 22, -1990404162),
          u = l(u, h, p, g, e[i + 12], 7, 1804603682),
          g = l(g, u, h, p, e[i + 13], 12, -40341101),
          p = l(p, g, u, h, e[i + 14], 17, -1502002290),
          h = l(h, p, g, u, e[i + 15], 22, 1236535329),
          u = c(u, h, p, g, e[i + 1], 5, -165796510),
          g = c(g, u, h, p, e[i + 6], 9, -1069501632),
          p = c(p, g, u, h, e[i + 11], 14, 643717713),
          h = c(h, p, g, u, e[i], 20, -373897302),
          u = c(u, h, p, g, e[i + 5], 5, -701558691),
          g = c(g, u, h, p, e[i + 10], 9, 38016083),
          p = c(p, g, u, h, e[i + 15], 14, -660478335),
          h = c(h, p, g, u, e[i + 4], 20, -405537848),
          u = c(u, h, p, g, e[i + 9], 5, 568446438),
          g = c(g, u, h, p, e[i + 14], 9, -1019803690),
          p = c(p, g, u, h, e[i + 3], 14, -187363961),
          h = c(h, p, g, u, e[i + 8], 20, 1163531501),
          u = c(u, h, p, g, e[i + 13], 5, -1444681467),
          g = c(g, u, h, p, e[i + 2], 9, -51403784),
          p = c(p, g, u, h, e[i + 7], 14, 1735328473),
          h = c(h, p, g, u, e[i + 12], 20, -1926607734),
          u = d(u, h, p, g, e[i + 5], 4, -378558),
          g = d(g, u, h, p, e[i + 8], 11, -2022574463),
          p = d(p, g, u, h, e[i + 11], 16, 1839030562),
          h = d(h, p, g, u, e[i + 14], 23, -35309556),
          u = d(u, h, p, g, e[i + 1], 4, -1530992060),
          g = d(g, u, h, p, e[i + 4], 11, 1272893353),
          p = d(p, g, u, h, e[i + 7], 16, -155497632),
          h = d(h, p, g, u, e[i + 10], 23, -1094730640),
          u = d(u, h, p, g, e[i + 13], 4, 681279174),
          g = d(g, u, h, p, e[i], 11, -358537222),
          p = d(p, g, u, h, e[i + 3], 16, -722521979),
          h = d(h, p, g, u, e[i + 6], 23, 76029189),
          u = d(u, h, p, g, e[i + 9], 4, -640364487),
          g = d(g, u, h, p, e[i + 12], 11, -421815835),
          p = d(p, g, u, h, e[i + 15], 16, 530742520),
          h = d(h, p, g, u, e[i + 2], 23, -995338651),
          u = f(u, h, p, g, e[i], 6, -198630844),
          g = f(g, u, h, p, e[i + 7], 10, 1126891415),
          p = f(p, g, u, h, e[i + 14], 15, -1416354905),
          h = f(h, p, g, u, e[i + 5], 21, -57434055),
          u = f(u, h, p, g, e[i + 12], 6, 1700485571),
          g = f(g, u, h, p, e[i + 3], 10, -1894986606),
          p = f(p, g, u, h, e[i + 10], 15, -1051523),
          h = f(h, p, g, u, e[i + 1], 21, -2054922799),
          u = f(u, h, p, g, e[i + 8], 6, 1873313359),
          g = f(g, u, h, p, e[i + 15], 10, -30611744),
          p = f(p, g, u, h, e[i + 6], 15, -1560198380),
          h = f(h, p, g, u, e[i + 13], 21, 1309151649),
          u = f(u, h, p, g, e[i + 4], 6, -145523070),
          g = f(g, u, h, p, e[i + 11], 10, -1120210379),
          p = f(p, g, u, h, e[i + 2], 15, 718787259),
          h = f(h, p, g, u, e[i + 9], 21, -343485551),
          u = r(u, n),
          h = r(h, o),
          p = r(p, a),
          g = r(g, s);
      return [u, h, p, g]
  }
  function h(e) {
      var t, i = "";
      for (t = 0; t < 32 * e.length; t += 8)
          i += String.fromCharCode(e[t >> 5] >>> t % 32 & 255);
      return i
  }
  function p(e) {
      var t, i = [];
      for (i[(e.length >> 2) - 1] = void 0,
      t = 0; t < i.length; t += 1)
          i[t] = 0;
      for (t = 0; t < 8 * e.length; t += 8)
          i[t >> 5] |= (255 & e.charCodeAt(t / 8)) << t % 32;
      return i
  }
  function g(e) {
      return h(u(p(e), 8 * e.length))
  }
  function m(e, t) {
      var i, n, o = p(e), r = [], a = [];
      for (r[15] = a[15] = void 0,
      o.length > 16 && (o = u(o, 8 * e.length)),
      i = 0; i < 16; i += 1)
          r[i] = 909522486 ^ o[i],
          a[i] = 1549556828 ^ o[i];
      return n = u(r.concat(p(t)), 512 + 8 * t.length),
      h(u(a.concat(n), 640))
  }
  function _(e) {
      var t, i, n = "0123456789abcdef", o = "";
      for (i = 0; i < e.length; i += 1)
          t = e.charCodeAt(i),
          o += n.charAt(t >>> 4 & 15) + n.charAt(15 & t);
      return o
  }
  function b(e) {
      return unescape(encodeURIComponent(e))
  }
  function F(e) {
      return g(b(e))
  }
  function v(e) {
      return _(F(e))
  }
  function y(e, t) {
      return m(b(e), b(t))
  }
  function w(e, t) {
      return _(y(e, t))
  }
  function x(e, t, i) {
      return t ? i ? y(t, e) : w(t, e) : i ? F(e) : v(e)
  }
  return x(e);
};

var get_as_cp = function() {
  var e = Math.floor((new Date).getTime() / 1e3)
    , t = e.toString(16).toUpperCase()
    , i = (0, _get_as_cp)(e).toString().toUpperCase();
  if (8 != t.length)
      return {
          as: "479BB4B7254C150",
          cp: "7E0AC8874BB0985"
      };
  for (var n = i.slice(0, 5), o = i.slice(-5), r = "", s = 0; s < 5; s++)
      r += n[s] + t[s];
  for (var l = "", c = 0; c < 5; c++)
      l += t[c + 3] + o[c];
  return {
      as: "A1" + r + t.slice(-3),
      cp: t.slice(0, 3) + l + "E1"
  }
};

var o ={};
var e = function(a) {
  var r = {
      exports: {},
      id: a,
      loaded: !1
  };
  return x.call(r.exports, r, r.exports, e),
      r.loaded = !0,
      r.exports
};

var x = function(t, e) {
  Function(function(t) {
      return 'e(e,a,r){(b[e]||(b[e]=t("x,y","x "+e+" y")(r,a)}a(e,a,r){(k[r]||(k[r]=t("x,y","new x[y]("+Array(r+1).join(",x[y]")(1)+")")(e,a)}r(e,a,r){n,t,s={},b=s.d=r?r.d+1:0;for(s["$"+b]=s,t=0;t<b;t)s[n="$"+t]=r[n];for(t=0,b=s=a;t<b;t)s[t]=a[t];c(e,0,s)}c(t,b,k){u(e){v[x]=e}f{g=,ting(bg)}l{try{y=c(t,b,k)}catch(e){h=e,y=l}}for(h,y,d,g,v=[],x=0;;)switch(g=){case 1:u(!)4:f5:u((e){a=0,r=e;{c=a<r;c&&u(e[a]),c}}(6:y=,u((y8:if(g=,lg,g=,y===c)b+=g;else if(y!==l)y9:c10:u(s(11:y=,u(+y)12:for(y=f,d=[],g=0;g<y;g)d[g]=y.charCodeAt(g)^g+y;u(String.fromCharCode.apply(null,d13:y=,h=delete [y]14:59:u((g=)?(y=x,v.slice(x-=g,y:[])61:u([])62:g=,k[0]=65599*k[0]+k[1].charCodeAt(g)>>>065:h=,y=,[y]=h66:u(e(t[b],,67:y=,d=,u((g=).x===c?r(g.y,y,k):g.apply(d,y68:u(e((g=t[b])<"<"?(b--,f):g+g,,70:u(!1)71:n72:+f73:u(parseInt(f,3675:if(){bcase 74:g=<<16>>16g76:u(k[])77:y=,u([y])78:g=,u(a(v,x-=g+1,g79:g=,u(k["$"+g])81:h=,[f]=h82:u([f])83:h=,k[]=h84:!085:void 086:u(v[x-1])88:h=,y=,h,y89:u({e{r(e.y,arguments,k)}e.y=f,e.x=c,e})90:null91:h93:h=0:;default:u((g<<16>>16)-16)}}n=this,t=n.Function,s=Object.keys||(e){a={},r=0;for(c in e)a[r]=c;a=r,a},b={},k={};r'.replace(/[-]/g, function(e) {
          return t[15 & e.charCodeAt(0)]
      })
  }("v[x++]=v[--x]t.charCodeAt(b++)-32function return ))++.substrvar .length(),b+=;break;case ;break}".split("")))()('gr$Daten Иb/s!l y͒yĹg,(lfi~ah`{mv,-n|jqewVxp{rvmmx,&effkx[!cs"l".Pq%widthl"@q&heightl"vr*getContextx$"2d[!cs#l#,*;?|u.|uc{uq$fontl#vr(fillTextx$$龘ฑภ경2<[#c}l#2q*shadowBlurl#1q-shadowOffsetXl#$$limeq+shadowColorl#vr#arcx88802[%c}l#vr&strokex[ c}l"v,)}eOmyoZB]mx[ cs!0s$l$Pb<k7l l!r&lengthb%^l$1+s$jl  s#i$1ek1s$gr#tack4)zgr#tac$! +0o![#cj?o ]!l$b%s"o ]!l"l$b*b^0d#>>>s!0s%yA0s"l"l!r&lengthb<k+l"^l"1+s"jl  s&l&z0l!$ +["cs\'(0l#i\'1ps9wxb&s() &{s)/s(gr&Stringr,fromCharCodes)0s*yWl ._b&s o!])l l Jb<k$.aj;l .Tb<k$.gj/l .^b<k&i"-4j!+& s+yPo!]+s!l!l Hd>&l!l Bd>&+l!l <d>&+l!l 6d>&+l!l &+ s,y=o!o!]/q"13o!l q"10o!],l 2d>& s.{s-yMo!o!]0q"13o!]*Ld<l 4d#>>>b|s!o!l q"10o!],l!& s/yIo!o!].q"13o!],o!]*Jd<l 6d#>>>b|&o!]+l &+ s0l-l!&l-l!i\'1z141z4b/@d<l"b|&+l-l(l!b^&+l-l&zl\'g,)gk}ejo{cm,)|yn~Lij~em["cl$b%@d<l&zl\'l $ +["cl$b%b|&+l-l%8d<@b|l!b^&+ q$sign ', [Object.defineProperty(e, "__esModule", {
      value: !0
  })])
};

var get_signature = function(_hot_time, ua){
  global.navigator = {
    userAgent: ua,
  };
  var a = 299;
  var tac = e(a);
  return tac.sign(_hot_time)
};