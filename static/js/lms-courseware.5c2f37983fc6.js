// Generated by CoffeeScript 1.3.3
(function() {

  this.Courseware = (function() {

    Courseware.prefix = '';

    function Courseware() {
      Courseware.prefix = $("meta[name='path_prefix']").attr('content');
      new Navigation;
      Logger.bind();
      this.render();
    }

    Courseware.start = function() {
      return new Courseware;
    };

    Courseware.prototype.render = function() {
      XModule.loadModules();
      return $('.course-content .histogram').each(function() {
        var histg, id;
        id = $(this).attr('id').replace(/histogram_/, '');
        try {
          histg = new Histogram(id, $(this).data('histogram'));
        } catch (error) {
          histg = error;
          if (typeof console !== "undefined" && console !== null) {
            console.log(error);
          }
        }
        return histg;
      });
    };

    return Courseware;

  })();

}).call(this);

// Generated by CoffeeScript 1.3.3
(function() {

  this.Histogram = (function() {

    function Histogram(id, rawData) {
      this.id = id;
      this.rawData = rawData;
      this.xTicks = [];
      this.yTicks = [];
      this.data = [];
      this.calculate();
      this.render();
    }

    Histogram.prototype.calculate = function() {
      var count, log_count, score, _i, _len, _ref, _ref1, _results;
      _ref = this.rawData;
      _results = [];
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        _ref1 = _ref[_i], score = _ref1[0], count = _ref1[1];
        if (score === null) {
          continue;
        }
        log_count = Math.log(count + 1);
        this.data.push([score, log_count]);
        this.xTicks.push([score, score.toString()]);
        _results.push(this.yTicks.push([log_count, count.toString()]));
      }
      return _results;
    };

    Histogram.prototype.render = function() {
      return $.plot($("#histogram_" + this.id), [
        {
          data: this.data,
          bars: {
            show: true,
            align: 'center',
            lineWidth: 0,
            fill: 1.0
          },
          color: "#b72121"
        }
      ], {
        xaxis: {
          min: -1,
          max: Math.max.apply(Math, $.map(this.xTicks, function(data) {
            return data[0] + 1;
          })),
          ticks: this.xTicks,
          tickLength: 0
        },
        yaxis: {
          min: 0.0,
          max: Math.max.apply(Math, $.map(this.yTicks, function(data) {
            return data[0] * 1.1;
          })),
          ticks: this.yTicks,
          labelWidth: 50
        }
      });
    };

    return Histogram;

  })();

}).call(this);

// Generated by CoffeeScript 1.3.3
(function() {

  this.Navigation = (function() {

    function Navigation() {
      var active;
      if ($('#accordion').length) {
        active = $('#accordion ul:has(li.active)').index('#accordion ul');
        if (active < 0) {
          active = $('#accordion h3.active').index('#accordion h3');
        }
        if (active < 0) {
          active = 0;
        }
        $('#accordion').bind('accordionchange', this.log).accordion({
          active: active,
          header: 'h3',
          autoHeight: false,
          heightStyle: 'content'
        });
        $('#accordion .ui-state-active').closest('.chapter').addClass('is-open');
        $('#open_close_accordion a').click(this.toggle);
        $('#accordion').show();
        $('#accordion a').click(this.setChapter);
      }
    }

    Navigation.prototype.log = function(event, ui) {
      return log_event('accordion', {
        newheader: ui.newHeader.text(),
        oldheader: ui.oldHeader.text()
      });
    };

    Navigation.prototype.toggle = function() {
      return $('.course-wrapper').toggleClass('closed');
    };

    Navigation.prototype.setChapter = function() {
      $('#accordion .is-open').removeClass('is-open');
      return $(this).closest('.chapter').addClass('is-open');
    };

    return Navigation;

  })();

}).call(this);

// Generated by CoffeeScript 1.3.3
(function() {
  var __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };

  this.Tab = (function() {

    function Tab(id, items) {
      this.id = id;
      this.items = items;
      this.onShow = __bind(this.onShow, this);

      this.el = $("#tab_" + id);
      this.render();
    }

    Tab.prototype.$ = function(selector) {
      return $(selector, this.el);
    };

    Tab.prototype.render = function() {
      var _this = this;
      $.each(this.items, function(index, item) {
        var tab;
        tab = $('<a>').attr({
          href: "#" + (_this.tabId(index))
        }).html(item.title);
        _this.$('.navigation').append($('<li>').append(tab));
        return _this.el.append($('<section>').attr({
          id: _this.tabId(index)
        }));
      });
      return this.el.tabs({
        show: this.onShow
      });
    };

    Tab.prototype.onShow = function(element, ui) {
      this.$('section.ui-tabs-hide').html('');
      this.$("#" + (this.tabId(ui.index))).html(this.items[ui.index]['content']);
      return this.el.trigger('contentChanged');
    };

    Tab.prototype.tabId = function(index) {
      return "tab-" + this.id + "-" + index;
    };

    return Tab;

  })();

}).call(this);
