// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-publications",
          title: "publications",
          description: "publications by categories in reversed chronological order.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-cv",
          title: "CV",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "news-graduated-from-the-university-of-toronto-with-a-b-a-sc-in-computer-engineering-with-high-honours",
          title: 'Graduated from the University of Toronto with a B.A.Sc. in Computer Engineering, with...',
          description: "",
          section: "News",},{id: "news-started-the-m-s-in-robotics-at-georgia-tech-joining-dr-glen-chou-s-trustworthy-robotics-lab",
          title: 'Started the M.S. in Robotics at Georgia Tech, joining Dr. Glen Chou’s Trustworthy...',
          description: "",
          section: "News",},{id: "news-two-papers-accepted-formal-safety-verification-and-refinement-for-generative-motion-planners-at-icra-2026-and-scalable-data-driven-reachability-analysis-and-control-via-koopman-operators-at-l4dc-2026",
          title: 'Two papers accepted: Formal Safety Verification and Refinement for Generative Motion Planners at...',
          description: "",
          section: "News",},{id: "news-released-the-preprint-pixels-to-proofs-probabilistically-safe-latent-world-model-control-via-parallel-conformal-robust-mpc-now-under-review-at-ra-l",
          title: 'Released the preprint Pixels to Proofs: Probabilistically-Safe Latent World Model Control via Parallel...',
          description: "",
          section: "News",},{id: "news-scalable-data-driven-reachability-analysis-and-control-via-koopman-operators-was-a-best-paper-award-finalist-at-l4dc-2026-1-8-acceptance-rate",
          title: 'Scalable Data-Driven Reachability Analysis and Control via Koopman Operators was a Best Paper...',
          description: "",
          section: "News",},{id: "news-started-the-phd-at-the-university-of-toronto-institute-for-aerospace-studies-joining-dr-steven-waslander-s-toronto-robotics-and-ai-laboratory-trail",
          title: 'Started the PhD at the University of Toronto Institute for Aerospace Studies, joining...',
          description: "",
          section: "News",},{id: "projects-project-1",
          title: 'project 1',
          description: "with background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/1_project/";
            },},{id: "projects-project-2",
          title: 'project 2',
          description: "a project with a background image and giscus comments",
          section: "Projects",handler: () => {
              window.location.href = "/projects/2_project/";
            },},{id: "projects-project-3-with-very-long-name",
          title: 'project 3 with very long name',
          description: "a project that redirects to another website",
          section: "Projects",handler: () => {
              window.location.href = "/projects/3_project/";
            },},{id: "projects-project-4",
          title: 'project 4',
          description: "another without an image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/4_project/";
            },},{id: "projects-project-5",
          title: 'project 5',
          description: "a project with a background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/5_project/";
            },},{id: "projects-project-6",
          title: 'project 6',
          description: "a project with no image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/6_project/";
            },},{id: "projects-project-7",
          title: 'project 7',
          description: "with background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/7_project/";
            },},{id: "projects-project-8",
          title: 'project 8',
          description: "an other project with a background image and giscus comments",
          section: "Projects",handler: () => {
              window.location.href = "/projects/8_project/";
            },},{id: "projects-project-9",
          title: 'project 9',
          description: "another project with an image 🎉",
          section: "Projects",handler: () => {
              window.location.href = "/projects/9_project/";
            },},{
        id: 'social-cv',
        title: 'CV',
        section: 'Socials',
        handler: () => {
          window.open("/assets/pdf/Haoran_Yin_CV.pdf", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=DjBNynMAAAAJ", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/danielyin21", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/haoran-yin-612a4b211", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
